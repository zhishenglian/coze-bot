# call_bot.py
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()                                      # ① 加载 .env
BOT_ID = "6gV4e78QjVw"                             # ② 你的 Bot ID
API_KEY = os.getenv("COZE_API_KEY")                # ③ 自动读 Token
URL = f"https://api.coze.cn/open_api/v2/chat"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def ask_bot(question: str):
    data = {
        "bot_id": BOT_ID,
        "user": "day4_user",
        "query": question,
        "stream": False
    }
    r = requests.post(URL, headers=HEADERS, data=json.dumps(data))
    return r.json()

if __name__ == "__main__":
    while True:
        q = input("你：")
        if q.lower() in ("quit", "q"):
            break
    ans = ask_bot(q)          # 先拿到返回
    if ans.get("code") == 4101:
    - 把第 33 行 `print` 改成：
```python
print("Bot：", ans["messages"][0]["content"])
    else:
        print("Bot:", ans["messages"][0]["content"])
