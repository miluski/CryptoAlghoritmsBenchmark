import pytest
from algorithms.classical import CaesarCipher, VigenereCipher
from algorithms.symmetric import AESCipher, DESCipher
from algorithms.asymmetric import RSACipher
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

def test_caesar_cipher():
    cipher = CaesarCipher(3)
    data = b"hello"
    encrypted = cipher.encrypt(data)
    decrypted = cipher.decrypt(encrypted)
    assert decrypted == data

def test_vigenere_cipher():
    cipher = VigenereCipher("KEY")
    data = b"hello"
    encrypted = cipher.encrypt(data)
    decrypted = cipher.decrypt(encrypted)
    assert decrypted == data

def test_aes_cipher():
    key = get_random_bytes(16)
    cipher = AESCipher(key)
    data = b"hello world"
    encrypted = cipher.encrypt(data)
    decrypted = cipher.decrypt(encrypted)
    assert decrypted == data

def test_des_cipher():
    key = get_random_bytes(8)
    cipher = DESCipher(key)
    data = b"hello"
    encrypted = cipher.encrypt(data)
    decrypted = cipher.decrypt(encrypted)
    assert decrypted == data

def test_rsa_cipher():
    key_pem = RSA.generate(2048).export_key()
    cipher = RSACipher(key_pem)
    data = b"hello"
    encrypted = cipher.encrypt(data)
    decrypted = cipher.decrypt(encrypted)
    assert decrypted == data
