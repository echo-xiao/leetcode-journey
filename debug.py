import os
import requests
from dotenv import load_dotenv  # 如果没有安装，请在终端运行: pip install python-dotenv

# 🚀 这一行是关键：它会读取你项目根目录下的 .env 文件
load_dotenv()

# ================= 配置区 =================
BASE_URL = "https://leetcode.com/"

# 🚀 从环境变量中读取真实的值，而不是使用变量名字符串
SESSION = os.getenv("LEETCODE_SESSION")
# 注意：确保这里的大小写和你 .env 文件里的一模一样
CSRF_TOKEN = os.getenv("LEETCODE_CSRFTOKEN")
# ==========================================

# ... 后面保持不变 ...

print(f"SESSION 编码检查: {[ord(c) for c in SESSION[:5]]}")
print(f"CSRF_TOKEN 编码检查: {[ord(c) for c in CSRF_TOKEN[:5]]}")


# ==========================================

def fetch_leetcode_final():
    url = f"{BASE_URL}/api/problems/all/"

    # 创建 Session 对象可以更稳定地保持持久连接
    s = requests.Session()

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "X-CSRFToken": CSRF_TOKEN,
        "Referer": BASE_URL,
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Connection": "keep-alive"
    }

    # 通过 cookies 参数传入，避开手动拼接字符串可能导致的 latin-1 编码错误
    cookies = {
        "LEETCODE_SESSION": SESSION,
        "csrftoken": CSRF_TOKEN
    }

    try:
        print(f"🚀 正在通过接口验证身份...")
        # 显式传入 cookies 字典，requests 会自动处理编码转换
        response = s.get(url, headers=headers, cookies=cookies, timeout=15)

        if response.status_code == 200:
            data = response.json()
            user_name = data.get("user_name", "")
            if user_name:
                print(f"✅ 登录成功！用户: {user_name}")
                print(f"📊 已通过题目总数: {data.get('num_solved', 0)}")
            else:
                print("⚠️ 响应成功但 user_name 为空，请检查 Token 是否真的对应当前域名。")
        else:
            print(f"❌ 请求失败，状态码: {response.status_code}")

    except Exception as e:
        print(f"💥 依然报错: {e}")
        print("\n💡 终极排查：请尝试在浏览器无痕模式下登录并重新获取一次新的 Token。")



if __name__ == "__main__":
    fetch_leetcode_final()