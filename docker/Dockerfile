# docker/Dockerfile
# Base image optimized for CUDA 12.1 and PyTorch 2.1.2
FROM pytorch/pytorch:2.1.2-cuda12.1-cudnn8-devel

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y git curl && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies (Resolving version conflicts)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the API port
EXPOSE 8000

# Set the default entrypoint for vLLM API Server
ENTRYPOINT ["python", "-m", "vllm.entrypoints.openai.api_server"]
