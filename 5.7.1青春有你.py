player_num = {}
li = []
print('请输入exit表示选手成绩录入完成')
while True:
    name = input("请输入选手名字：\n")
    if name == 'exit':
        break
    score = float(input("请输入选手票数：\n"))
    player_num[name] = score
items = player_num.items()
for j in items:
    li.append([j[1], j[0]])
li.sort()
count = len(li) - 1
for i in range(1, len(li) + 1):
    print(f"第{i}名：{li[count][1]},成绩为{li[count][0]}分")
    count -= 1