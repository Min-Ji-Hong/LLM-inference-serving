# Efficient Distributed LLM Inference on the Cloud

> Building a scalable, cost-effective serving system for open-source LLMs — from a single legacy GPU to a distributed multi-GPU cloud cluster.

**Graduation Project (Capstone)** — College of Data Science, Hanyang University
**Advisor:** Prof. Kyungyong Lee (DDPS Lab)
**Team:** Jihong Min, Byungyoon Chung
**Period:** 2026.03 – 2026.12 (in progress)

---

## Overview

Serving large language models efficiently is a major engineering challenge — naive scripts hit memory bottlenecks and poor GPU utilization under concurrent load. This project builds a production-style distributed inference system using **vLLM** (PagedAttention) for open-source LLMs, progressing from a single constrained local GPU to a distributed, cost-optimized multi-GPU cloud deployment.

## My Role

- System architecture design and vLLM local/cloud deployment
- Cloud orchestration and distributed system architecture (tensor/pipeline parallelism across multi-GPU cloud instances)

*(Byungyoon Chung: Docker containerization, API authentication security, load testing/benchmarking)*

## Approach

1. **Local baseline (single GPU)** — Serve Gemma-2b on a legacy NVIDIA Tesla P100. Default FP32 caused out-of-memory crashes; switching to half-precision (`dtype=half`) produced a stable baseline with predictable latency and a smaller KV-cache footprint.
2. **OpenAI-compatible API layer** — Hosted a REST API server compliant with the OpenAI protocol, validating async networking and multi-turn chat templates.
3. **Containerization** — Packaged the vLLM stack into a multi-stage Docker image, resolving version conflicts between `transformers`, the CUDA runtime, and vLLM's compiled core to produce a deterministic, cloud-ready artifact.
4. **Security middleware** — Added token-based API key authentication ahead of cloud deployment.
5. **Cloud migration & Tensor Parallelism (Completed)** — Successfully migrated to an AWS EC2 multi-GPU instance (4x A10G). Implemented Tensor Parallelism (`--tensor-parallel-size 4`) to split intra-layer weights via NCCL, eliminating memory fragmentation.
6. **Stress Testing & Benchmarking (Completed)** — Executed high-volume concurrency tests (100+ users). Validated that the distributed cloud setup maintains a highly responsive Time-To-First-Token (TTFT) of 0.43s and a throughput of 380+ tokens/sec with zero OOM events.

## Infrastructure

| | |
|---|---|
| **Local Testbed** | Intel Xeon E5-1620 v4, 128GB RAM, dual NVIDIA Tesla P100 (16GB VRAM each) |
| **Cloud Testbed** | AWS EC2 `g5.12xlarge` (4x NVIDIA A10G GPUs) |
| **Base Model** | Gemma-2b |
| **Serving Engine** | vLLM (PagedAttention, NCCL Distributed Backend) |

## Status

**As of October 2026:** We have successfully completed the cloud migration, Tensor Parallelism implementation, and extreme concurrency load testing. We are currently finalizing the structured cost-efficiency financial models and eradicating remaining inter-node data-transfer bottlenecks in preparation for the final capstone defense in December.

## Repo Structure

```text
├── docs/
│   ├── Proposal.pdf 
│   ├── ProgressReport_1.pdf      # Initial phase (Local P100 & Containerization)
│   ├── ProgressReport_2.pdf      # [NEW] Phase 2 (Cloud TP & Benchmarking)
│   └── ConferenceReport.pdf
├── docker/
│   ├── Dockerfile                # Multi-stage vLLM container
│   └── requirements.txt          # Dependency pinning to prevent drift
├── scripts/
│   └── run_distributed_cloud.sh  # Multi-GPU execution script
├── benchmarks/
│   └── stress_test.py            # Async payload for concurrency testing
└── logs/                         # Raw telemetry and execution logs
    ├── local_p100_init.log
    ├── cloud_a10g_tp.log
    └── benchmark_stress_test.log
