sinfo = {"xiaohong": 0, "xiaolan": 0, "xiaoming": 1, "xiaobai": 1}
new_info = {}  # 创建一个空字典用于存储满足条件的项
for name, gender in sinfo.items():  # 遍历原始字典的键值对
    if gender == 0:  # 检查条件：性别为0的项
        new_info[name] = gender

print(f"修改后的的员工信息为：{new_info}")


# sinfo = {"xiaohong": 0, "xiaolan": 0, "xiaoming": 1, "xiaobai": 1}
# for key in [name for name, gender in sinfo.items() if gender == 1]:
#     del sinfo[key]
# print('修改后的的员工信息为：')
# print(sinfo)