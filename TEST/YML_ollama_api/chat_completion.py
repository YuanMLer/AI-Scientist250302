from openai import OpenAI

#连接本地搭建的ollam模型

client = OpenAI(
    # base_url="http://192.168.31.172:11434/v1",
    base_url="http://192.168.31.172:11434/v1",
    api_key="ollama-api-key"  # required, but unused

)

response = client.completions.create(
  model="qwen3:32b",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)

print(response)