import os
import numpy as np
from algorithms.classical import CaesarCipher, VigenereCipher
from algorithms.symmetric import AESCipher, DESCipher
from algorithms.asymmetric import RSACipher
from measurement.performance import PerformanceMeasurer
from plotting.plotter import Plotter
from data.generator import DataGenerator
from keys.manager import KeyManager
from benchmark.runner import BenchmarkRunner

def main():
    os.makedirs("results/keys", exist_ok=True)
    os.makedirs("results/samples", exist_ok=True)

    iterations = 3

    key_manager = KeyManager()
    key_manager.generate_keys()
    key_manager.save_keys()

    measurer = PerformanceMeasurer()
    plotter = Plotter()
    generator = DataGenerator()
    runner = BenchmarkRunner(measurer, plotter, generator)

    classical_symmetric_sizes = [10000, 100000, 1000000, 10000000, 50000000, 100000000, 200000000]
    asymmetric_sizes = classical_symmetric_sizes

    algorithm_suites = {
        "Classical": {
            "Caesar": CaesarCipher(key_manager.get_key("Caesar")),
            "Vigenere": VigenereCipher(key_manager.get_key("Vigenere")),
        },
        "Symmetric": {
            "AES-128": AESCipher(key_manager.get_key("AES-128")),
            "AES-192": AESCipher(key_manager.get_key("AES-192")),
            "AES-256": AESCipher(key_manager.get_key("AES-256")),
            "DES": DESCipher(key_manager.get_key("DES")),
        },
        "Asymmetric": {
            "RSA-2048": RSACipher(key_manager.get_key("RSA-2048")),
        }
    }

    with open("results/benchmark_results.txt", "w") as f:
        f.write("Cryptographic Keys Used (for documentation):\n")
        f.write(f"Caesar Shift: {key_manager.get_key('Caesar')}\n")
        f.write(f"Vigenere Key: {key_manager.get_key('Vigenere')}\n")
        f.write(f"AES-128 Key (hex): {key_manager.get_key('AES-128').hex()}\n")
        f.write(f"AES-192 Key (hex): {key_manager.get_key('AES-192').hex()}\n")
        f.write(f"AES-256 Key (hex): {key_manager.get_key('AES-256').hex()}\n")
        f.write(f"DES Key (hex): {key_manager.get_key('DES').hex()}\n")
        f.write("RSA-2048 Key (PEM):\n")
        f.write(key_manager.get_key("RSA-2048").decode('utf-8'))
        f.write("\n\n")
        runner.run_suite("Classical", algorithm_suites["Classical"], classical_symmetric_sizes, iterations, f, key_manager.keys)
        runner.run_suite("Symmetric", algorithm_suites["Symmetric"], classical_symmetric_sizes, iterations, f, key_manager.keys)
        runner.run_suite("Asymmetric", algorithm_suites["Asymmetric"], asymmetric_sizes, iterations, f, key_manager.keys)

if __name__ == "__main__":
    main()
