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
