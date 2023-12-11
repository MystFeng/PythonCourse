bad_words = ["傻逼", "智障", "蠢", "滚", "死", "操", "你妈", "狗东西"]
original_input = input("骂人试试：")
result = original_input

for word in bad_words:
    if word in result:
        result = result.replace(word, "*" * len(word))

if result == original_input:
    print("未检测到敏感词。")
else:
    print(f"脏话已被替换为：{result}")