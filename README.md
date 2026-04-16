# M5-SLR-Benchmark

# Benchmarking Apple M5 Unified Memory for Real-Time Sign Language Recognition

## Overview
This repository contains the benchmarking suite and experimental data for the study: 
**"On-Device vs. Cloud-Based Inference: Benchmarking Apple M5 Unified Memory Architecture against Virtualized Tensor Core Accelerators for Sign Language Recognition."**

## Abstract
[cite_start]Seamless human-computer interaction for sign language recognition (SLR) demands deterministic, low-latency inference[cite: 6]. [cite_start]This study benchmarks a MediaPipe-based system across local Apple M5 silicon, Google Colab CPU (Intel Xeon), and T4 GPU instances[cite: 8]. [cite_start]Experimental results using a 1,705-frame workload demonstrate that the Apple M5 achieves a mean latency of 17.02 ms and a throughput of 58.75 FPS[cite: 9].

## Key Features
* [cite_start]**Headless Benchmarking:** Isolates core hardware performance by bypassing GUI rendering overhead[cite: 73, 76].
* [cite_start]**Feature Extraction:** Implements a 21-point hand landmark model (63-value feature vector)[cite: 58].
* [cite_start]**Architectural Analysis:** Compares the 2nm Apple M5 Unified Memory Architecture (UMA) against 12nm discrete cloud GPUs[cite: 69, 70].

## Results
| Platform | Mean Latency (ms) | Std Dev (ms) | Throughput (FPS) |
| :--- | :--- | :--- | :--- |
| **Apple M5 (Edge)** | **17.02** | **1.98** | **58.75** |
| Nvidia T4 (Cloud) | 18.09 | 4.60 | 55.27 |
| Intel Xeon (CPU) | 29.27 | 5.18 | 34.17 |

[cite_start]*The Apple M5 demonstrated superior temporal stability, being 132% more stable than the cloud-based T4 GPU[cite: 11].*

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Run benchmark: `python scripts/benchmark.py --headless`
