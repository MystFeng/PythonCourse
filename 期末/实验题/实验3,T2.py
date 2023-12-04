sinfo = {"xiaohong": 0, "xiaolan": 0, "xiaoming": 1, "xiaobai": 1}
new_info = {}
for name, gender in sinfo.items():
    new_info[name] = gender if gender == 0 else None
print(f"修改后的的员工信息为：{new_info}")