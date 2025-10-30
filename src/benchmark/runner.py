import os
import numpy as np
from measurement.performance import PerformanceMeasurer
from plotting.plotter import Plotter
from data.generator import DataGenerator

class BenchmarkRunner:
    def __init__(self, measurer, plotter, generator):
        self.measurer = measurer
        self.plotter = plotter
        self.generator = generator

    def run_suite(self, suite_name, algorithms, sizes, iterations, log_file, keys):
        suite_results = self._initialize_results(algorithms)
        self._write_suite_header(suite_name, log_file)
        for size in sizes:
            self._run_size_tests(size, algorithms, iterations, suite_results, log_file)
        self.plotter.plot_results(suite_name, suite_results, sizes)

    def _initialize_results(self, algorithms):
        return {alg: {"encrypt_time": [], "decrypt_time": [], "encrypt_cpu": [], "decrypt_cpu": [], "encrypt_mem": [], "decrypt_mem": []} for alg in algorithms}

    def _write_suite_header(self, suite_name, log_file):
        header = f"\n{'='*20}\n {suite_name} BENCHMARK \n{'='*20}\n"
        print(header)
        log_file.write(header)

    def _run_size_tests(self, size, algorithms, iterations, suite_results, log_file):
        text = self.generator.generate_random_text(size)
        data = text.encode('latin-1')
        self._save_sample(text, size)
        self._write_size_header(size, iterations, log_file)
        for name, cipher in algorithms.items():
            encrypt_metrics, decrypt_metrics = self._run_algorithm_tests(cipher, data, iterations)
            avg_encrypt = {k: np.mean(v) for k, v in encrypt_metrics.items()}
            avg_decrypt = {k: np.mean(v) for k, v in decrypt_metrics.items()}
            self._update_results(suite_results, name, avg_encrypt, avg_decrypt)
            self._write_result_line(name, avg_encrypt, avg_decrypt, log_file)

    def _save_sample(self, text, size):
        with open(f"results/samples/sample_{size}_chars.txt", "w") as sf:
            sf.write(text)

    def _write_size_header(self, size, iterations, log_file):
        header = f"\n--- Testing {size / 1024:.0f} KB ({size} characters) over {iterations} iterations ---\n"
        print(header)
        log_file.write(header)

    def _run_algorithm_tests(self, cipher, data, iterations):
        encrypt_iter = {"time": [], "cpu": [], "mem": []}
        decrypt_iter = {"time": [], "cpu": [], "mem": []}
        for _ in range(iterations):
            encrypted = cipher.encrypt(data)
            encrypt_metrics = self.measurer.measure(cipher.__class__, "encrypt", data, cipher.get_key_data())
            decrypt_metrics = self.measurer.measure(cipher.__class__, "decrypt", encrypted, cipher.get_key_data())
            for k in encrypt_iter:
                encrypt_iter[k].append(encrypt_metrics[k])
            for k in decrypt_iter:
                decrypt_iter[k].append(decrypt_metrics[k])
        return encrypt_iter, decrypt_iter

    def _update_results(self, suite_results, name, avg_encrypt, avg_decrypt):
        for m_key in suite_results[name]:
            if 'encrypt' in m_key:
                suite_results[name][m_key].append(avg_encrypt[m_key.replace('encrypt_', '')])
            elif 'decrypt' in m_key:
                suite_results[name][m_key].append(avg_decrypt[m_key.replace('decrypt_', '')])

    def _write_result_line(self, name, avg_encrypt, avg_decrypt, log_file):
        result_line = f"{name:<10} | encrypt: {avg_encrypt['time']:.5f}s CPU:{avg_encrypt['cpu']:.2f}% MEM:{avg_encrypt['mem']:.4f}MB | decrypt: {avg_decrypt['time']:.5f}s CPU:{avg_decrypt['cpu']:.2f}% MEM:{avg_decrypt['mem']:.4f}MB\n"
        print(result_line, end="")
        log_file.write(result_line)
