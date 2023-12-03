user_input = input("请输入一个字符串: ")
# 提取下标为偶数的字符
list1 = []
for i in range(0, len(user_input), 2):
    list1.append(user_input[i])
# 提取下标为奇数的字符
list2 = []
for i in range(1, len(user_input), 2):
    list2.append(user_input[i])
# 将A和B连接起来
combined_list = list1 + list2
print(f"合并后的列表：{combined_list}")