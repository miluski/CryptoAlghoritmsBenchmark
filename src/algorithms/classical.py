from .base import Cipher

class CaesarCipher(Cipher):
    def __init__(self, shift_or_key_data):
        if isinstance(shift_or_key_data, int):
            self.shift = shift_or_key_data
        else:
            self.shift = shift_or_key_data

    def encrypt(self, data: bytes) -> bytes:
        return self._shift_text(data.decode('latin-1'), self.shift).encode('latin-1')

    def decrypt(self, data: bytes) -> bytes:
        return self._shift_text(data.decode('latin-1'), -self.shift).encode('latin-1')

    def get_key_data(self):
        return self.shift

    def _shift_text(self, text: str, shift: int) -> str:
        result = ""
        for char in text:
            if 'a' <= char <= 'z':
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += char
        return result

class VigenereCipher(Cipher):
    def __init__(self, key_or_key_data):
        if isinstance(key_or_key_data, str):
            self.key = [ord(k.lower()) - ord('a') for k in key_or_key_data]
        else:
            self.key = key_or_key_data

    def encrypt(self, data: bytes) -> bytes:
        return self._vigenere_text(data.decode('latin-1'), self.key).encode('latin-1')

    def decrypt(self, data: bytes) -> bytes:
        return self._vigenere_text(data.decode('latin-1'), [-k for k in self.key]).encode('latin-1')

    def get_key_data(self):
        return self.key

    def _vigenere_text(self, text: str, key_shifts) -> str:
        key_len = len(key_shifts)
        result = ""
        for i, char in enumerate(text):
            shift = key_shifts[i % key_len]
            if 'a' <= char <= 'z':
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += char
        return result
