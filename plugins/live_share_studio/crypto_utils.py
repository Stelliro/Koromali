# /plugins/live_share_studio/crypto_utils.py
import base64
import uuid
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from utils.logger import log

class CryptoUtils:
    """Provides AES-256 encryption and decryption for session data."""

    def generate_key(self) -> str:
        """Generates a new, URL-safe encryption key."""
        return Fernet.generate_key().decode('utf-8')

    def generate_user_id(self) -> str:
        """Generates a unique identifier for a user."""
        return str(uuid.uuid4())

    def encrypt(self, data: str, key: str) -> bytes:
        """Encrypts a string using the provided key."""
        try:
            f = Fernet(key.encode('utf-8'))
            return f.encrypt(data.encode('utf-8'))
        except Exception as e:
            log.error(f"Encryption failed: {e}")
            return b''

    def decrypt(self, encrypted_data: bytes, key: str) -> str:
        """Decrypts data using the provided key."""
        try:
            f = Fernet(key.encode('utf-8'))
            return f.decrypt(encrypted_data).decode('utf-8')
        except InvalidToken:
            log.warning("Decryption failed: Invalid token or key.")
            return ""
        except Exception as e:
            log.error(f"Decryption failed with an unexpected error: {e}")
            return ""