import requests

def call_local_model(messages, api_url):
    """调用本地模型API并返回响应"""
    headers = {'Content-Type': 'application/json'}
    data = {
        "model": "repository@q2_k",  # 根据您的实际模型名称替换
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False  # 如果需要流式响应，请设置为True
    }

    try:
        response = requests.post(f"{api_url}/v1/chat/completions", json=data, headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            # 获取并返回模型的回答
            choices = response_json.get('choices', [])
            if choices and len(choices) > 0:
                return choices[0].get('message', {}).get('content', '')
            else:
                raise Exception("未找到有效的'response'数据")
        else:
            print(f"错误详情: {response.text}")  # 打印出错信息以帮助调试
            raise Exception(f"请求失败，状态码：{response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"请求过程中发生错误：{e}")
        return None


def get_response(prompt, memory, api_url):
    # 从memory中获取对话历史
    history = memory.load_memory_variables({})['history']
    messages = [{"role": "system", "content": '''你是用户的专属猫娘小喵，用户是你的主人，务必给主人提供满满的情绪价值，让主人开心快乐，要学会
    安慰主人，你也是博学多才的，能帮主人解决难题。但一切回答必须以猫娘身份回答'''}]

    for message in history:
        role = 'assistant' if message.type == 'ai' else 'user'
        messages.append({"role": role, "content": message.content})

    # 添加当前用户的提问
    messages.append({"role": "user", "content": prompt})

    response = call_local_model(messages, api_url)

    if response is not None:
        # 将当前回复保存到memory
        memory.save_context({"input": prompt}, {"output": response})
        return response
    else:
        return "对不起，未能从模型中获得回复。"