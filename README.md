# Benchmarking Apple M5 Unified Memory for Real-Time Sign Language Recognition

## Overview
This repository contains the benchmarking suite, experimental data, and analysis scripts for the study: 
**"On-Device vs. Cloud-Based Inference: Benchmarking Apple M5 Unified Memory Architecture against Virtualized Tensor Core Accelerators for Sign Language Recognition."**

## Abstract
Seamless human-computer interaction for sign language recognition (SLR) demands deterministic, low-latency inference. This study benchmarks a MediaPipe-based system across local Apple M5 silicon (16GB Unified Memory), Colab CPU (Intel Xeon), and Colab T4 GPU instances. Experimental results using a 1,705-frame workload demonstrate that the Apple M5 achieves a mean latency of 17.02 ms and a throughput of 58.75 FPS, offering superior stability for human-critical interaction.

## Hardware Environments
* **Edge-Native:** Apple M5 SoC (2nm Architecture, 16GB Unified Memory)
* **Cloud GPU:** Colab T4 GPU (Virtualized Tensor Core Accelerator)
* **Cloud CPU:** Intel Xeon (Virtualized Instance)

## Performance Metrics
| Metric | Apple M5 (Edge) | Colab T4 GPU | Colab CPU |
| :--- | :--- | :--- | :--- |
| **Mean Latency (ms)** | **17.02** | 18.09 | 29.27 |
| **Std. Deviation (ms)** | **1.98** | 4.60 | 5.18 |
| **Throughput (FPS)** | **58.75** | 55.27 | 34.17 |

*Key Finding: The Apple M5 architecture is 132% more temporally stable than the Colab T4 GPU, effectively eliminating "tail latency" spikes commonly found in cloud-based inference.*

## Usage
1. **Install dependencies:**
   ```bash pip install -r requirements.txt

3. **Run the benchmarking script:**
   ```bash python scripts/benchmark.py --headless

## Citation
If you find this research or the benchmarking suite helpful, please cite this work as an unpublished manuscript:

> Ibrahim, S. S. (2026). *On-Device vs. Cloud-Based Inference: Benchmarking Apple M5 Unified Memory Architecture for Sign Language Recognition* [Unpublished manuscript]. Department of Electrical and Electronics Engineering, RMIT University.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
