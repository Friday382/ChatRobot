import streamlit as st
from langchain.memory import ConversationBufferMemory

from local_utils import get_response

# 左侧导航栏
with st.sidebar:
    if st.button('返回'):
        st.switch_page('pages/main1.py')
    API_KEY = st.text_input('请输入本地模型API')
    st.markdown('[获取通义API_KEY](https://bailian.console.aliyun.com/?apiKey=1#/api-key)')


# 标题
st.title('test1')

# 创建会话体,用于存储对话历史
if 'memory' not in st.session_state:
    st.session_state['memory'] = ConversationBufferMemory(return_messages=True)
    st.session_state['messages'] = [
        {'role': 'ai', 'content': '主人您好，我是您的专属猫娘小喵~请尽情吩咐小喵吧！'}
    ]

# 创建消息区,用于显示对话历史
for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# 创建文本,用于输入问题
prompt = st.chat_input('请输入问题')
if prompt:
    if not API_KEY:
        st.warning('请先输入API_KEY')
        st.stop()

    # 把用户消息加入会话体，并打印
    st.session_state['messages'].append({'role': 'human', 'content': prompt})
    st.chat_message('human').markdown(prompt)

    # 调用AI接口,获取回答,加入等待提示
    with st.spinner('思考中...'):
        response = get_response(prompt, st.session_state['memory'], API_KEY)

    # 把AI回答加入会话体,并打印
    st.session_state['messages'].append({'role': 'ai', 'content': response})
    st.chat_message('ai').markdown(response)
