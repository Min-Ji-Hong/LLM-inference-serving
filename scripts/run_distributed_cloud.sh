#!/bin/bash
# scripts/run_distributed_cloud.sh
# Multi-GPU Tensor Parallelism Execution Script for AWS EC2 (4x A10G)

export VLLM_API_KEY="sk-hanyang-capstone-2026"
export MODEL_NAME="google/gemma-2b-it"

echo "Starting vLLM Distributed Inference Server..."
echo "Model: $MODEL_NAME | Tensor Parallel Size: 4"

python -m vllm.entrypoints.openai.api_server \
    --host 0.0.0.0 \
    --port 8000 \
    --model $MODEL_NAME \
    --dtype half \
    --tensor-parallel-size 4 \
    --gpu-memory-utilization 0.95 \
    --enforce-eager
