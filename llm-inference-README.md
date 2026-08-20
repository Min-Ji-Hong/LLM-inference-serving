# Efficient Distributed LLM Inference on the Cloud

> Building a scalable, cost-effective serving system for open-source LLMs — from a single legacy GPU to a distributed multi-GPU cloud cluster.

**Graduation Project (Capstone)** — College of Data Science, Hanyang University
**Advisor:** Prof. Kyungyong Lee (DDPS Lab)
**Team:** Jihong Min, Byungyoon Chung
**Period:** 2026.03 – 2026.12 (in progress)

---

## Overview

Serving large language models efficiently is a major engineering challenge — naive
scripts hit memory bottlenecks and poor GPU utilization under concurrent load. This
project builds a production-style distributed inference system using **vLLM**
(PagedAttention) for open-source LLMs, progressing from a single constrained local
GPU to a distributed, cost-optimized multi-GPU cloud deployment.

## My Role

- System architecture design and vLLM local/cloud deployment
- Cloud orchestration and distributed system architecture (tensor/pipeline
  parallelism across multi-GPU cloud instances)

*(Byungyoon Chung: Docker containerization, API authentication security, load
testing/benchmarking)*

## Approach

1. **Local baseline (single GPU)** — Serve Gemma-2b on a legacy NVIDIA Tesla P100
   (Pascal architecture, no native FP16 Tensor Cores). Default FP32 caused
   out-of-memory crashes; switching to half-precision (`dtype=half`) produced a
   stable baseline with predictable latency and a smaller KV-cache footprint.
2. **OpenAI-compatible API layer** — Hosted a REST API server compliant with the
   OpenAI protocol, validating async networking, token decoding, and multi-turn chat
   templates.
3. **Containerization** — Packaged the vLLM stack into a multi-stage Docker image
   (PyTorch base), resolving version conflicts between `transformers`, the CUDA
   runtime, and vLLM's compiled core to produce a deterministic, cloud-ready
   artifact.
4. **Security middleware** — Added token-based API key authentication ahead of
   cloud deployment.
5. **Cloud migration (in progress)** — Deploy to AWS/GCP multi-GPU instances;
   implement tensor parallelism (intra-layer weight splitting via NVLink) and
   pipeline parallelism (sequential layer segmentation) to host larger models with
   minimized inter-node latency.
6. **Benchmarking (planned)** — Stress-test with simulated concurrent traffic,
   measuring Time-To-First-Token, inter-token latency, and throughput (tokens/sec),
   then build a cost-efficiency model comparing local vs. cloud GPU economics.

## Infrastructure

| | |
|---|---|
| Local testbed | Intel Xeon E5-1620 v4, 128GB RAM, dual NVIDIA Tesla P100 (16GB VRAM each) |
| Base model | Gemma-2b |
| Serving framework | vLLM (PagedAttention) |
| Target cloud | AWS or GCP (multi-GPU instances) |

## Status

Currently in the containerization and security-hardening phase (as of June 2026),
preparing for cloud migration and distributed benchmarking in the second half of the
project. Final deliverable includes a benchmarking-driven cost/performance analysis
and a manuscript draft targeting an AI systems / cloud computing venue.

## Repo Structure

```
├── docs/          # progress reports, proposal
├── src/           # (실제 코드가 있다면 여기에)
├── docker/        # Dockerfiles
└── README.md
```

## References

- Kwon, W., et al. (2023). "Efficient Memory Management for Large Language Model
  Serving with PagedAttention." *SOSP '23*.
- Blancas, E. (2024). "Deploying vLLM: a Step-by-Step Guide." Ploomber Blog.
- Lee, S., et al. (2022). "PROFET: PROFiling-based CNN Training Latency ProphET for
  GPU Cloud Instances." *IEEE Big Data*.
- Choi, J., et al. (2022). "All-You-Can-Inference: Serverless DNN Model Inference
  Suite." *ACM/IFIP Middleware Workshop*.
