from .base import Cipher
from Crypto.Cipher import AES, DES

class AESCipher(Cipher):
    def __init__(self, key_or_key_data):
        self.key = key_or_key_data

    def encrypt(self, data: bytes) -> bytes:
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        return cipher.nonce + tag + ciphertext

    def decrypt(self, data: bytes) -> bytes:
        nonce = data[:16]
        tag = data[16:32]
        ciphertext = data[32:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
        return cipher.decrypt_and_verify(ciphertext, tag)

    def get_key_data(self):
        return self.key

class DESCipher(Cipher):
    def __init__(self, key_or_key_data):
        self.key = key_or_key_data

    def encrypt(self, data: bytes) -> bytes:
        cipher = DES.new(self.key, DES.MODE_ECB)
        pad_len = 8 - len(data) % 8
        data_padded = data + bytes([pad_len]) * pad_len
        return cipher.encrypt(data_padded)

    def decrypt(self, data: bytes) -> bytes:
        cipher = DES.new(self.key, DES.MODE_ECB)
        decrypted = cipher.decrypt(data)
        pad_len = decrypted[-1]
        return decrypted[:-pad_len]

    def get_key_data(self):
        return self.key
