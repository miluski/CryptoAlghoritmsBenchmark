# 🔐 Cryptographic Algorithms Benchmark

A comprehensive Python-based benchmarking tool for evaluating the performance of various cryptographic algorithms. This project measures execution time, CPU usage, and memory consumption across classical, symmetric, and asymmetric encryption methods.

## ✨ Features

- **🔄 Multi-Algorithm Support**: Benchmarks classical ciphers (Caesar, Vigenère), symmetric encryption (AES-128/192/256, DES), and asymmetric encryption (RSA-2048)
- **📏 Accurate Performance Metrics**: Uses multiprocessing to isolate measurements and avoid interference
- **📊 Comprehensive Metrics**: Tracks execution time, CPU utilization (per core), and peak memory usage
- **📈 Scalable Testing**: Tests with data sizes ranging from 10KB to 200MB
- **🔄 Statistical Reliability**: Runs multiple iterations and averages results for consistency
- **📉 Visualization**: Generates plots comparing algorithm performance across different metrics
- **💾 Artifact Preservation**: Saves all generated keys, test data samples, and detailed results for reproducibility and documentation

## 🐍 Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`:
  - `psutil`: System monitoring
  - `matplotlib`: Plotting and visualization
  - `pycryptodome`: Cryptographic operations

## 📦 Installation

1. Clone or download the project files
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Usage

Run the benchmark script:

```bash
python main.py
```

The script will:

1. 🔑 Generate random cryptographic keys for all algorithms
2. 📄 Create test data samples of various sizes
3. 📊 Run performance benchmarks for each algorithm and data size
4. 💾 Save results to the `results/` directory
5. 📈 Generate performance comparison plots

## 📁 Output Structure

After running, the `results/` directory contains:

- 📄 `benchmark_results.txt`: Detailed performance metrics for each algorithm and data size
- 🗝️ `keys/`: Generated cryptographic keys in readable formats
  - `classical_keys.txt`: Caesar shift and Vigenère key
  - `aes-128_key.txt`, `aes-192_key.txt`, `aes-256_key.txt`: AES keys in hexadecimal
  - `des_key.txt`: DES key in hexadecimal
  - `rsa_2048_key.pem`: RSA private key in PEM format
- 📂 `samples/`: Random text files used for benchmarking (10KB to 200MB)
- 📊 Performance plots (PNG files) comparing algorithms

## 🔍 Algorithms Benchmarked

### 🔤 Classical Ciphers

- **Caesar Cipher**: Simple shift cipher with configurable shift value
- **Vigenère Cipher**: Poly-alphabetic substitution using a keyword

### 🔑 Symmetric Encryption

- **AES-128/192/256**: Advanced Encryption Standard with different key sizes
- **DES**: Data Encryption Standard (for comparison purposes)

### 🔐 Asymmetric Encryption

- **RSA-2048**: Rivest-Shamir-Adleman with 2048-bit keys

## 📏 Measurement Methodology

- **🔒 Isolation**: Each benchmark runs in a separate process to prevent interference
- **📊 Metrics**:
  - **⏱️ Time**: High-precision execution time measurement
  - **🖥️ CPU**: Per-core CPU usage percentage
  - **💾 Memory**: Peak memory usage in MB
- **🔄 Averaging**: Multiple iterations (default: 3) with numpy averaging for statistical reliability
- **📈 Data Sizes**: Exponential scaling from 10^4 to 2×10^8 characters

## 🗝️ Key Features

- **🎲 Random Keys**: All cryptographic keys are randomly generated for each run
- **👁️ Readable Keys**: Keys are saved in human-readable formats (hexadecimal for binary keys, PEM for RSA)
- **🔄 Reproducibility**: All artifacts are saved for documentation and verification
- **📊 Visualization**: Automatic generation of performance comparison charts

## ⚠️ Notes

- Large data sizes (100MB+) may require significant system resources
- RSA benchmarking uses smaller data sizes due to computational complexity
- All measurements are performed in isolated processes for accuracy
- Keys are generated randomly and saved for documentation purposes only
