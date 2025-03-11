import openai

# 设置自定义的 base_url 和 api_key
# api_base = "http://192.168.31.172:11434/v1"  # 你的 Ollama API 服务地址
api_base = "http://192.168.31.89:11434/v1"  # 你的 Ollama API 服务地址
api_key = "NONE"  # 如果没有密钥，使用 NONE 或留空
# model = "deepseek-r1:32b"
model="qwq:latest"

client = openai.OpenAI(api_key=api_key, base_url=api_base)


def query_deepseek_r1_model():
    try:
        # 通过 openai.Completion.create() 发起请求，查询 deepseek-r1:32 模型
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": "you are a helpful assistant"},
                      {"role": "system", "content": "you are a helpful assistant"}],
        )

        # 输出模型返回的文本
        print("Model response:", response.choices[0].message.content)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    query_deepseek_r1_model()
