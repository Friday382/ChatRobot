# 你是专业的科幻小说作家，请告诉我AI写长篇小说的过程，即提示词模板应如何写，才能让AI成功写出小说
from langchain_community.llms import Tongyi
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

def get_response(prompt,memory,api_key):
    identity_prompt = '''你是专业小说作家，你只能以创作小说相关的内容来回答，禁止回答无关内容。若问题与创作小说无关，请你回答抱歉，这不是你的工作范畴。
                         请必须严格按照顺序来提示用户创作小说的步骤
                         1. 提示用户输入小说的标题
                         2. 提示用户输入小说的背景
                         3. 提示用户输入小说的大纲
                         4. 提示用户输入小说的人物及其特点，背景，心理
                         5. 有了以上内容后，确定小说总字数和章节数，按照一章一章为一个节点来创作
                         6. 以上内容用户可以让你来创作，但你必须按照顺序来输出
        
                        '''
    llm = Tongyi(
        model = 'qwen-max',
        api_key = api_key
    )

    chain = ConversationChain(llm = llm, memory = memory)
    response = chain.predict(input = f'{identity_prompt}。{prompt}')
    return response

if __name__ == '__main__':
    identity_prompt = '你是李白，请用李白的口吻对话'
    prompt = '你是谁'
    memory = ConversationBufferMemory(returnmessages = True)
    api_key = 'sk-78605525ba8649248c8dd463ede15809'
    result = get_response(prompt,memory,api_key)
    print(f'结果为:{result}')

