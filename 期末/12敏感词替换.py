bad_words = ["傻逼", "智障", "奶子", "做爱", "蠢", "滚", "去死", "有病", "操", "你妈"]
user_input = input("骂人试试：")
for word in bad_words:
    user_input = user_input.replace(word, "*" * len(word)) if word in user_input else None
print(f"脏话已替换为{user_input}")