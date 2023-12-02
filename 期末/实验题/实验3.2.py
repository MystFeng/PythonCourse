sinfo = {"xiaohong": 0, "xiaolan": 0, "xiaoming": 1, "xiaobai": 1}
filtered_sinfo = {name: gender for name, gender in sinfo.items() if gender == 0}

print('修改后的的员工信息为：')
for name, gender in filtered_sinfo.items():
    print(f"{name}: {gender}")

# sinfo = {"xiaohong": 0, "xiaolan": 0, "xiaoming": 1, "xiaobai": 1}
# for key in [name for name, gender in sinfo.items() if gender == 1]:
#     del sinfo[key]
# print('修改后的的员工信息为：')
# print(sinfo)