# Benchmarking Apple M5 Unified Memory for Real-Time Sign Language Recognition

## Overview
This repository contains the benchmarking suite and experimental data for the study: 
**"On-Device vs. Cloud-Based Inference: Benchmarking Apple M5 Unified Memory Architecture against Virtualized Tensor Core Accelerators for Sign Language Recognition."**

## Abstract
Seamless human-computer interaction for sign language recognition (SLR) demands deterministic, low-latency inference. This study benchmarks a MediaPipe-based system across local Apple M5 silicon (16GB Unified Memory), Colab CPU (Intel Xeon), and Colab T4 GPU instances. Experimental results using a 1,705-frame workload demonstrate that the Apple M5 achieves a mean latency of 17.02 ms and a throughput of 58.75 FPS.

## Hardware Environments
* **Edge-Native:** Apple M5 SoC (2nm Architecture, Unified Memory)
* **Cloud GPU:** Colab T4 GPU (Virtualized Tensor Core Accelerator)
* **Cloud CPU:** Intel Xeon (Virtualized Instance)

## Results
| Performance Metric | Apple M5 (Edge) | Colab T4 GPU | Colab CPU |
| :--- | :--- | :--- | :--- |
| **Mean Latency (ms)** | **17.02** | 18.09 | 29.27 |
| **Std. Deviation (ms)** | **1.98** | 4.60 | 5.18 |
| **Throughput (FPS)** | **58.75** | 55.27 | 34.17 |

*Findings show the Apple M5 is 132% more temporally stable than the Colab T4 GPU, effectively eliminating the "tail latency" spikes observed in cloud environments.*

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Execute benchmark: `python scripts/benchmark.py --headless`

## Citation
Please cite this work if used in your research:
> Ibrahim, S. S. (2026). On-Device vs. Cloud-Based Inference: Benchmarking Apple M5 Unified Memory Architecture for Sign Language Recognition. RMIT University.
