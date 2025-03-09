import streamlit as st
import mysql.connector
from mysql.connector import Error
import time
# 连接到MySQL数据库函数
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='localhost'
        )
        if connection.is_connected():
            print('Connected to MySQL database')
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# 检查用户名是否存在
def check_username_exists(username):
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM login_in WHERE user_name=%s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result is not None

# 注册新用户
def register_user(username, password):
    if check_username_exists(username):
        return False
    conn = create_connection()
    cursor = conn.cursor()
    query = "INSERT INTO login_in (user_name, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    conn.commit()
    cursor.close()
    conn.close()
    return True

# 验证用户登录
def validate_login(username, password):
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM login_in WHERE user_name=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result is not None

# Streamlit界面
st.title("用户注册与登录")

# 切换状态
if 'view' not in st.session_state:
    st.session_state.view = '登录'

# 自定义CSS
st.markdown("""
<style>
.stButton > button:first-child {
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# 布局
if st.session_state.view == "注册":
    st.subheader("创建新账户")
    new_user = st.text_input("用户名", key="new_user")
    new_passwd = st.text_input("密码", type='password', key="new_passwd")
    if st.button("注册"):
        if register_user(new_user, new_passwd):
            st.success("您已成功创建账户!")
            # 通过设置默认值为空字符串间接“清空”输入框
            st.session_state.get("new_user", "")
            st.session_state.get("new_passwd", "")
            time.sleep(1)  # 延迟一秒
            st.session_state.view = "登录"
            st.rerun()  # 强制刷新页面
        else:
            st.error("用户名已存在，请选择另一个用户名。")
else:
    st.subheader("登录区域")
    username = st.text_input("用户名", key="login_user")
    password = st.text_input("密码", type='password', key="login_passwd")
    if st.button("登录"):
        if validate_login(username, password):
            st.success("登录成功！")
            # 使用Streamlit原生页面跳转功能（推荐方式）
            try:
                # 适用于Streamlit >= 1.28.0
                st.switch_page("pages/main1.py")
            except AttributeError:
                # 兼容旧版本的JavaScript跳转
                js = """
                        <script>
                            window.location.pathname = "/test1";
                        </script>
                    """
                st.components.v1.html(js)
        else:
            st.warning("用户名或密码错误。")
        # 通过设置默认值为空字符串间接“清空”输入框
        st.session_state.get("login_user", "")
        st.session_state.get("login_passwd", "")

# 切换按钮
if st.button("切换到" + ("登录" if st.session_state.view == "注册" else "注册")):
    st.session_state.view = "登录" if st.session_state.view == "注册" else "注册"
    st.rerun()  # 强制刷新页面


