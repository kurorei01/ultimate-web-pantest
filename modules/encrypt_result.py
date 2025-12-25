from cryptography.fernet import Fernet
from typing import Union

def encrypt_result(result: str, key: Union[str, bytes]) -> bytes:
    # Convert key to bytes if it's a string
    key_bytes = key.encode() if isinstance(key, str) else key
    f = Fernet(key_bytes)
    return f.encrypt(result.encode())