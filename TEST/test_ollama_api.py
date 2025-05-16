import requests, json
OLLAMA_URL = "http://192.168.31.172:11434/api/generate"
MODEL = "qwen3:32b"
prompt = "Hello, who are you?"
data = {"model": MODEL, "prompt": prompt}
resp = requests.post(OLLAMA_URL, json=data)
result = resp.json()
print(result)
#print(result["response"])  # The model's reply
