from .base import Cipher
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

class RSACipher(Cipher):
    def __init__(self, key_or_key_data):
        if isinstance(key_or_key_data, str):
            key_pem = key_or_key_data.encode('utf-8')
        else:
            key_pem = key_or_key_data
        self.key = RSA.import_key(key_pem)
        self.cipher_enc = PKCS1_OAEP.new(self.key.publickey())
        self.cipher_dec = PKCS1_OAEP.new(self.key)

    def encrypt(self, data: bytes) -> bytes:
        chunk_size = 190
        encrypted_chunks = [self.cipher_enc.encrypt(data[i:i+chunk_size]) for i in range(0, len(data), chunk_size)]
        return b"".join(encrypted_chunks)

    def decrypt(self, data: bytes) -> bytes:
        chunk_size = 256
        decrypted_chunks = [self.cipher_dec.decrypt(data[i:i+chunk_size]) for i in range(0, len(data), chunk_size)]
        return b"".join(decrypted_chunks)

    def get_key_data(self):
        return self.key.export_key(format='PEM').decode('utf-8')
