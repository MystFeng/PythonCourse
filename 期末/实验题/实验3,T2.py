sinfo = {"xiaohong": 0, "xiaolan": 0, "xiaoming": 1, "xiaobai": 1}
new_info = {}
for name, gender in sinfo.items():
    new_info[name] = gender if gender == 0 else None
print(f"修改后的的员工信息为：{new_info}")

# 其他方法：
# sinfo = {"xiaohong": 0, "xiaolan": 0, "xiaoming": 1, "xiaobai": 1}
# filtered_sinfo = {name: gender for name, gender in sinfo.items() if gender == 0}
# print(f"修改前的信息:{sinfo}")
# print(f"修改后的信息:{filtered_sinfo}")