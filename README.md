### 项目启动
在项目根目录下进入终端，输入 streamlit run login.py
### 文件介绍
login.py 是启动界面文件  
pages文件里是其他界面文件,streamlit只能自动识别pages目录下的页面  
utils.py是调用线上大模型API交互的核心函数文件  
local_utils.py是调用本地大模型的文件  
pages/main.py是调用线上大模型API的界面  
pages/main1.py是本地调用的界面  
pages/test1.py是本地调用界面的下一个页面,目前没有做功能  
### 如何调用模型
线上API,目前做的是阿里云百炼平台里的 qwen-max 模型,输入自己申请的百炼的API即可  
本地模型，输入OPENAI兼容格式的即可，代码中已经补全了/v1/chat/completions，只需要输入 http://127.0.0.1:1234 类似的地址即可  
