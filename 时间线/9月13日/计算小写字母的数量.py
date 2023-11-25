# 普通运算
# strs = "AbcDeFGhIJ"
# count = 0
# for j in strs:
#     for j in strs.lower():
#         count += 1 if j == j else 0
# print(count)


# ？类似三目运算
# strs = "AbcDeFGhIJ"
# lowercase_count = sum(1 for char in strs if char.islower())
# print(lowercase_count)


# 三目运算符
s = 'AbcDeFGhIJ'
lowercase_count = sum(1 if char.islower() else 0 for char in s)
print({lowercase_count})