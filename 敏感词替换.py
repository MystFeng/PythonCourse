sensitive_words = ["傻逼", "智障", "奶子", "做爱", "蠢", "滚", "去死", "有病", "操", "你妈"]
input_content = input("骂人试试：")
for word in sensitive_words:
    if word in input_content:
        input_content = input_content.replace(word, "*" * len(word))
print(f"你的话被替换成了{input_content}")
