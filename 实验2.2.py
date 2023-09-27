# 1) 创建一个空列表 score
score = []

# 2) 追加10个数值
score.extend([68, 87, 92, 100, 76, 88, 54, 89, 76, 61])

# 3) 输出第3个元素的数值
print(f"第3个元素的数值为: {score[2]}")

# 4) 输出第1~6个元素的值
print(f"第1~6个元素的值为: {score[:6]}")

# 5) 在第3个元素之前添加数值59
score.insert(2, 59)

# 6) 查询数值76在score列表中出现的次数
num = 76
count_76 = score.count(num)
print(f"{num} 在列表中出现了 {count_76} 次")

# 7) 查询数值76是否在score列表中
if num in score:
    print(f"{num} 在列表中")

# 8) 查询满分的学生学号
perfect_score_index = score.index(100)
print(f"满分学生的学号是: {perfect_score_index + 1}")

# 9) 将59分加1分
score[score.index(59)] += 1

# 10) 删除第1个元素
del score[0]

# 11) 获取元素个数
num_of_elements = len(score)
print(f"元素个数为: {num_of_elements}")

# 12) 对列表进行排序
score.sort()
print(f"最低分是: {score[0]}, 最高分是: {score[-1]}")

# 13) 颠倒元素顺序
score.reverse()

# 14) 删除尾部元素
removed_element = score.pop()

# 15) 追加88并删除第一个88
score.append(88)
score.remove(88)

# 16) 合并两个列表
score1 = [80, 61]
score2 = [71, 95, 82]
merged_score = score1 + score2
print(f"合并后的列表为: {merged_score}")

# 17) 复制score1中元素5遍到score2中
score2 = score1 * 5
print(f"复制后的score2列表为: {score2}")
