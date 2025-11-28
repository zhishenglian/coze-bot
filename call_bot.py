import json

fake = {
    "messages": [{
        "content": "2112 可能指年份、编号或数字组合，具体要看上下文。",
        "role": "assistant"
    }]
}

print(200, json.dumps(fake, ensure_ascii=False))
