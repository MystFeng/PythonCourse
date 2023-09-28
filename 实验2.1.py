user_input = input("请输入一个字符串: ")
# 提取下标为偶数的字符
list_A = [user_input[i] for i in range(0, len(user_input), 2)]
# 提取下标为奇数的字符
list_B = [user_input[i] for i in range(1, len(user_input), 2)]
# 将A和B连接起来
combined_list = list_A + list_B
print("合并后的列表:", combined_list)
