# 整数求和，输入整数n，计算1~n之和
sum = 0
n = int(input("输入n:"))
for i in range(n + 1):
    sum += i
print(sum)