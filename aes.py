from Crypto.Cipher import AES  # type: ignore
from Crypto.Util.Padding import pad, unpad  # type: ignore
import base64

def normalize_key(key_str):
    key_bytes = key_str.encode('utf-8')
    return key_bytes[:16].ljust(16, b'\0')

def encrypt_aes_128(plain_text, key):
    try:
        key = normalize_key(key)
        cipher = AES.new(key, AES.MODE_ECB)
        padded_text = pad(plain_text.encode('utf-8'), AES.block_size)
        encrypted_bytes = cipher.encrypt(padded_text)
        return base64.b64encode(encrypted_bytes).decode('utf-8')
    except Exception as e:
        return f"Encryption error: {str(e)}"

def decrypt_aes_128(cipher_text, key):
    try:
        key = normalize_key(key)
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted = cipher.decrypt(base64.b64decode(cipher_text))
        return unpad(decrypted, AES.block_size).decode('utf-8')
    except Exception:
        return "Wrong decryption key or ciphertext corrupted"
