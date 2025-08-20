# /plugins/live_share_studio/collaboration_client.py
import asyncio
import websockets
import json
from PyQt6.QtCore import QThread, pyqtSignal

from app_core.koromali_api import KoromaliPluginAPI
from .crypto_utils import CryptoUtils
from utils.logger import log

class CollaborationClient(QThread):
    """Manages the client-side connection to the collaboration server."""
    connection_successful = pyqtSignal()
    connection_failed = pyqtSignal(str)
    disconnected = pyqtSignal()
    
    # Decrypted data signals
    text_update_received = pyqtSignal(dict)
    cursor_update_received = pyqtSignal(dict)
    file_switched_received = pyqtSignal(dict)
    file_locked_received = pyqtSignal(str, str) # file_path, user_id
    file_unlocked_received = pyqtSignal(str) # file_path
    user_list_updated = pyqtSignal(dict)
    permission_denied = pyqtSignal(str)
    edit_log_received = pyqtSignal(dict)

    def __init__(self, crypto: CryptoUtils, api: KoromaliPluginAPI):
        super().__init__()
        self.crypto = crypto
        self.api = api
        self.loop, self.websocket, self.uri = None, None, None
        self.user_id, self.username, self.encryption_key = None, None, None
        self._is_running = True

    def run(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        try:
            self.loop.run_until_complete(self._listen())
        except Exception as e:
            log.error(f"Client event loop error: {e}", exc_info=True)

    async def _listen(self):
        try:
            async with websockets.connect(self.uri) as ws:
                self.websocket = ws
                log.info(f"Client connected to {self.uri}")
                # Send join message to register with the server
                await self._send_raw_message({
                    "type": "join",
                    "payload": {
                        "username": self.username,
                        "user_id": self.user_id
                    }
                })
                
                async for message in self.websocket:
                    if not self._is_running: break
                    try:
                        decrypted_message = self.crypto.decrypt(message, self.encryption_key)
                        if not decrypted_message:
                            log.warning("Received an undecryptable message from server.")
                            continue
                        
                        data = json.loads(decrypted_message)
                        msg_type = data.get("type")
                        payload = data.get("payload", {})
                        
                        if msg_type == "welcome":
                            self.user_id = payload.get("user_id") # Server confirms/assigns user ID
                            self.user_list_updated.emit(payload.get("users", {}))
                            if "shared_projects" in payload:
                                self.api.get_main_window().set_shared_paths(payload["shared_projects"])
                            self.connection_successful.emit()
                        elif msg_type == "user_list_update":
                            self.user_list_updated.emit(payload.get("users", {}))
                        elif msg_type == "text_update":
                            self.text_update_received.emit(payload)
                        elif msg_type == "permission_denied":
                            self.permission_denied.emit(payload.get("reason", "No reason provided."))
                        elif msg_type == "edit_log_response":
                            self.edit_log_received.emit(payload.get("log", {}))
                        # Add other message types here...

                    except json.JSONDecodeError:
                        log.warning("Received invalid JSON from server.")
                    except Exception as e:
                        log.error(f"Error processing server message: {e}", exc_info=True)
                        
        except Exception as e:
            self.connection_failed.emit(f"Failed to connect or listen: {e}")
        finally:
            self.api.get_main_window().set_shared_paths([])
            self.disconnected.emit()
            log.info("Client disconnected.")

    def connect_to_server(self, uri: str, username: str, user_id: str, key: str):
        self.uri, self.username, self.user_id, self.encryption_key = uri, username, user_id, key
        self._is_running = True
        self.start()

    def disconnect(self):
        self._is_running = False
        if self.loop and self.loop.is_running():
            asyncio.run_coroutine_threadsafe(self._shutdown_client_tasks(), self.loop)
        self.quit()
        self.wait()

    async def _shutdown_client_tasks(self):
        if self.websocket and self.websocket.open:
            await self.websocket.close()
        # This stops the event loop, which will terminate the `run` method
        if self.loop.is_running():
            self.loop.stop()
        
    def is_connected(self) -> bool:
        return self.websocket is not None and self.websocket.open

    async def _send_raw_message(self, message: dict):
        if self.is_connected():
            await self.websocket.send(json.dumps(message))

    def send_message(self, message_type: str, payload: dict):
        """Encrypts and sends a message to the server."""
        if not self.is_connected() or not self.loop or not self.loop.is_running():
            log.warning(f"Message send failed: client not ready (connected: {self.is_connected()}, loop: {self.loop.is_running() if self.loop else 'None'})")
            return

        message = {
            "type": message_type,
            "payload": payload,
            "user_id": self.user_id
        }
        json_message = json.dumps(message)
        encrypted_message = self.crypto.encrypt(json_message, self.encryption_key)
        
        if encrypted_message:
            future = asyncio.run_coroutine_threadsafe(
                self.websocket.send(encrypted_message), self.loop
            )
            try:
                future.result(timeout=2)
            except Exception as e:
                log.error(f"Failed to send message to server: {e}")