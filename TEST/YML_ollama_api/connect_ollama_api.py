from openai import OpenAI

#连接本地搭建的ollam模型

client = OpenAI(
    # base_url="http://192.168.31.172:11434/v1",
    base_url="http://192.168.31.172:11434/v1",
    api_key="ollama-api-key"  # required, but unused

)

response = client.chat.completions.create(
    # model = "deepseek-r1:32b",
    model="qwen3:32b",
    messages=[
        {"role":"system", "content":"you are a helpful assistant"},
        {"role":"system", "content":"Who won the world series in 2020?"},
    ]
)
print(response.choices[0].message.content)