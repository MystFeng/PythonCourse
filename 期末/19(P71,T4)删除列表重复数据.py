# 常规for方法
# li_one = [1, 2, 1, 2, 3, 5, 4, 3, 5, 7, 4, 7, 8]
# li_two=[]
# for i in li_one:
#     if i in li_two:
#         pass
#     else:
#         li_two.append(i)
# print(li_two)

# 利用集合的不重复性（更简洁）
li_one = [1, 2, 1, 2, 3, 5, 4, 3, 5, 7, 4, 7, 8]
li_two = list(set(li_one))
print(li_two)