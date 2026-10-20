# benchmarks/stress_test.py
import asyncio
import aiohttp
import time

API_URL = "http://localhost:8000/v1/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-hanyang-capstone-2026" # API Key Security
}

PAYLOAD = {
    "model": "google/gemma-2b-it",
    "prompt": "Explain the concept of quantum computing in 3 paragraphs.",
    "max_tokens": 150,
    "temperature": 0.7
}

async def fetch(session, request_id):
    start_time = time.time()
    async with session.post(API_URL, headers=HEADERS, json=PAYLOAD) as response:
        await response.json()
        ttft = time.time() - start_time
        return ttft

async def run_stress_test(concurrency=100, total_requests=2500):
    print(f"Starting Stress Test | Concurrency: {concurrency} | Total: {total_requests}")
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, i) for i in range(total_requests)]
        results = await asyncio.gather(*tasks)
        
        avg_ttft = sum(results) / len(results)
        print(f"Test Completed. Average TTFT: {avg_ttft:.3f} seconds")

if __name__ == "__main__":
    # Simulate 100 concurrent users mimicking real-world chatbot traffic
    asyncio.run(run_stress_test(concurrency=100, total_requests=2500))
