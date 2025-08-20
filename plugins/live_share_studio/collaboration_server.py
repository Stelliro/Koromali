# /plugins/live_share_studio/collaboration_server.py
import asyncio
import websockets
import json
import uuid
import socket
import time
from pathlib import Path
from PyQt6.QtCore import QThread, pyqtSignal
from .crypto_utils import CryptoUtils
from utils.logger import log

class CollaborationServer(QThread):
    """Runs an asyncio WebSocket server for the collaborative session."""
    server_started = pyqtSignal(str, int, str)
    server_stopped = pyqtSignal()
    log_message = pyqtSignal(str)
    user_joined = pyqtSignal(dict)
    user_left = pyqtSignal(str)

    def __init__(self, crypto: CryptoUtils):
        super().__init__()
        self.crypto = crypto
        self.loop = None
        self.server = None
        self.host = '0.0.0.0'
        self.port = 8765
        
        # New state management
        self.connections = {} # {websocket: user_id}
        self.users = {}       # {user_id: {"ws": websocket, "username": str}}
        self.user_roles = {}  # {user_id: [role_name]}
        self.roles = {
            "Host": {"permissions": {"*": "rw"}}, # Host can do anything
            "Guest": {"permissions": {}}          # Guest can do nothing by default
        }
        self.permissions = {} # {norm_path: {"default": "r/w/rw/none", "users": {uid: "r/w"}, "roles": {role: "r/w"}}}
        self.edit_log = {}    # {filepath: [{"user_id":..., "timestamp":..., "diff":...}]}
        self.shared_projects = []
        
        self._is_running = True
        self.host_user_id = None

    def set_session_data(self, key: str, shared_projects: list):
        self.encryption_key = key
        self.shared_projects = [str(Path(p).resolve()) for p in shared_projects]
        self._initialize_permissions()

    def _initialize_permissions(self):
        """Sets the initial deny-all policy for shared projects."""
        self.permissions = {}
        for project_path in self.shared_projects:
            # By default, no one has access. Host permissions are handled by role.
            self.permissions[project_path] = {"default": "deny"}

    def run(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        try:
            start_server = websockets.serve(self._handler, self.host, self.port)
            self.server = self.loop.run_until_complete(start_server)
            
            # Find a non-local IP to display to the user
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.connect(("8.8.8.8", 80))
                    ip_address = s.getsockname()[0]
            except Exception:
                ip_address = "127.0.0.1"

            self.server_started.emit(ip_address, self.port, "session123")
            self.log_message.emit(f"Server started on {ip_address}:{self.port}")
            self.loop.run_forever()
        except Exception as e:
            self.log_message.emit(f"Server thread error: {e}")
            log.error(f"Server thread error: {e}", exc_info=True)
        finally:
            if self.loop.is_running(): self.loop.close()
            self.server_stopped.emit()

    def _check_permission(self, user_id: str, file_path: str, action: str) -> bool:
        """Check if a user has permission for an action on a file."""
        if user_id == self.host_user_id:
            return True # Host can always do anything
        
        # TODO: Implement a full-fledged permission checking logic
        # For now, we deny all guests to meet the initial security requirement.
        return False

    async def _handler(self, websocket, path):
        user_id = None
        try:
            async for message in websocket:
                if not self._is_running: break
                
                # First message from a new client must be an unencrypted 'join'
                if websocket not in self.connections:
                    try:
                        data = json.loads(message)
                        if data.get("type") == "join":
                            payload = data.get("payload", {})
                            user_id = payload.get("user_id") or str(uuid.uuid4())
                            username = payload.get("username", "Anonymous")

                            if not self.users: # First user to connect is the host
                                self.host_user_id = user_id
                                self.user_roles[user_id] = ["Host"]
                                self.log_message.emit(f"Host '{username}' ({user_id}) connected.")
                            else:
                                self.user_roles[user_id] = ["Guest"]
                                self.log_message.emit(f"User '{username}' ({user_id}) joined.")

                            self.connections[websocket] = user_id
                            self.users[user_id] = {"ws": websocket, "username": username}

                            welcome_payload = {
                                "user_id": user_id,
                                "users": self._get_user_list_payload(),
                                "shared_projects": self.shared_projects
                            }
                            await self._send_to_client(websocket, "welcome", welcome_payload)
                            
                            await self.broadcast("user_list_update", {"users": self._get_user_list_payload()})
                        else:
                            log.warning("First message was not 'join'. Disconnecting.")
                            break
                    except json.JSONDecodeError:
                        log.warning("Server received malformed JSON on join. Disconnecting.")
                        break
                    continue

                # Subsequent messages are encrypted
                try:
                    decrypted_message = self.crypto.decrypt(message, self.encryption_key)
                    if not decrypted_message:
                        log.warning("Could not decrypt message.")
                        continue
                    
                    data = json.loads(decrypted_message)
                    sender_id = data.get("user_id")
                    
                    # --- Message Handling with Permissions ---
                    msg_type = data.get("type")
                    msg_payload = data.get("payload", {})
                    
                    if msg_type == "text_update":
                        file_path = msg_payload.get("file_path")
                        if self._check_permission(sender_id, file_path, "write"):
                            # Log the edit
                            if file_path not in self.edit_log: self.edit_log[file_path] = []
                            self.edit_log[file_path].append({
                                "user_id": sender_id,
                                "timestamp": time.time(),
                                "diff": msg_payload.get("diff")
                            })
                            await self.broadcast(decrypted_message, sender_ws=websocket)
                        else:
                            await self._send_to_client(websocket, "permission_denied", {"reason": f"No write access to {file_path}"})
                    elif msg_type == "get_edit_log":
                        if sender_id == self.host_user_id:
                            await self._send_to_client(websocket, "edit_log_response", {"log": self.edit_log})
                    else:
                        # For other messages, broadcast without checks for now
                        await self.broadcast(decrypted_message, sender_ws=websocket)

                except json.JSONDecodeError:
                    log.warning("Server received malformed JSON in encrypted message.")
                except Exception as e:
                    log.error(f"Error in server handler: {e}", exc_info=True)

        finally:
            if websocket in self.connections:
                user_id = self.connections.pop(websocket)
                departing_user = self.users.pop(user_id, {})
                self.user_roles.pop(user_id, None)
                self.log_message.emit(f"User '{departing_user.get('username', 'Unknown')}' disconnected.")
                await self.broadcast("user_list_update", {"users": self._get_user_list_payload()})

    def _get_user_list_payload(self) -> dict:
        """Constructs the user list payload with roles."""
        return {
            uid: {
                "name": u_data["username"], 
                "roles": self.user_roles.get(uid, [])
            } for uid, u_data in self.users.items()
        }

    def start_server(self, host='0.0.0.0', port=8765):
        self.host, self.port = host, port
        self._is_running = True
        self.start()

    def stop(self):
        self._is_running = False
        if self.server:
            self.server.close()
            # Need to run a task to wait for the server to close
            if self.loop and self.loop.is_running():
                 self.loop.call_soon_threadsafe(lambda: asyncio.ensure_future(self.server.wait_closed()))
        if self.loop and self.loop.is_running():
            self.loop.call_soon_threadsafe(self.loop.stop)
        self.quit()
        self.wait()

    def is_running(self) -> bool:
        return self.isRunning()

    async def _send_to_client(self, client_ws, msg_type: str, payload: dict):
        message = {"type": msg_type, "payload": payload}
        json_message = json.dumps(message)
        encrypted_message = self.crypto.encrypt(json_message, self.encryption_key)
        if encrypted_message:
            await client_ws.send(encrypted_message)

    async def broadcast(self, message: str, sender_ws=None):
        if not self.connections: return
        # The message is already decrypted JSON string from the sender
        # Re-encrypt for each recipient
        encrypted_message = self.crypto.encrypt(message, self.encryption_key)
        if encrypted_message:
            tasks = [ws.send(encrypted_message) for ws in self.connections if ws != sender_ws]
            if tasks:
                await asyncio.gather(*tasks)