# 普通运算
# s = "AbcDeFGhIJ"
# count = 0
# for i in s:
#     for j in s.lower():
#         count += 1 if i == j else 0
# print(count)


# ？类似三目运算
# s = "AbcDeFGhIJ"
# lowercase_count = sum(1 for char in s if char.islower())
# print(lowercase_count)


# 三目运算符
s = 'AbcDeFGhIJ'
lowercase_count = sum(1 if char.islower() else 0 for char in s)
print({lowercase_count})