import random
import string
import os
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

class KeyManager:
    def __init__(self):
        self.keys = {}

    def generate_keys(self):
        self.keys = {
            "Caesar": random.randint(1, 25),
            "Vigenere": ''.join(random.choice(string.ascii_uppercase) for _ in range(10)),
            "AES-128": get_random_bytes(16),
            "AES-192": get_random_bytes(24),
            "AES-256": get_random_bytes(32),
            "DES": get_random_bytes(8),
            "RSA-2048": RSA.generate(2048).export_key()
        }

    def save_keys(self):
        os.makedirs("results/keys", exist_ok=True)
        with open("results/keys/classical_keys.txt", "w") as f:
            f.write(f"Caesar Shift: {self.keys['Caesar']}\n")
            f.write(f"Vigenere Key: {self.keys['Vigenere']}\n")
        for name in ["AES-128", "AES-192", "AES-256", "DES"]:
            with open(f"results/keys/{name.lower()}_key.txt", "w") as f:
                f.write(f"{name} Key (hex): {self.keys[name].hex()}\n")
        with open("results/keys/rsa_2048_key.pem", "wb") as f:
            f.write(self.keys["RSA-2048"])

    def get_key(self, name):
        return self.keys[name]
