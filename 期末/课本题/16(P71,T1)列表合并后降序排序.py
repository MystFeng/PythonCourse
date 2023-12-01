# 共有两种方法：
# 1.使用extend()方法
# li_num1=[4,5,2,7]
# li_num2=[3,6]
# li_num1.extend(li_num2)
# li_num1.sort(reverse=True)
# print(li_num1)

# 2.使用+号
li_num1 = [4, 5, 2, 7]
li_num2 = [3, 6]
li_num3 = li_num1 + li_num2
li_num3.sort(reverse=True)
print(li_num3)