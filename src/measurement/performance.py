import time
import psutil
import tempfile
import os
from multiprocessing import Process, Queue

class PerformanceMeasurer:
    def measure(self, cipher_class, method_name, data, key_data):
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(data)
            data_file = f.name
        queue = Queue()
        p = Process(target=self._target_func, args=(queue, cipher_class, method_name, data_file, key_data))
        p.start()
        peak_mem = self._monitor_memory(p)
        p.join()
        os.unlink(data_file)
        results = queue.get()
        results["mem"] = peak_mem / (1024 ** 2)
        results["cpu"] = results["cpu"] / psutil.cpu_count()
        return results

    def _target_func(self, queue, cipher_class, method_name, data_file, key_data):
        with open(data_file, 'rb') as f:
            data = f.read()
        cipher = cipher_class(key_data)
        process = psutil.Process()
        process.cpu_percent(interval=None)
        time.sleep(0.1)
        start = time.perf_counter()
        getattr(cipher, method_name)(data)
        elapsed = time.perf_counter() - start
        cpu_usage = process.cpu_percent(interval=None)
        queue.put({"time": elapsed, "cpu": cpu_usage})

    def _monitor_memory(self, p):
        try:
            ps_p = psutil.Process(p.pid)
            peak_mem = 0
            while p.is_alive():
                try:
                    mem_info = ps_p.memory_info()
                    current_mem = mem_info.uss if hasattr(mem_info, 'uss') else mem_info.rss
                    if current_mem > peak_mem:
                        peak_mem = current_mem
                except psutil.NoSuchProcess:
                    break
                time.sleep(0.01)
        except psutil.NoSuchProcess:
            peak_mem = 0
        return peak_mem
