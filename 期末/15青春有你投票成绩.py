scores = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}
while True:
    name = input("请输入选手名字(按Q退出)：")
    if name.lower() == 'q':
        break
    score = float(input("请输入选手成绩："))
    scores[name] = score

sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(sorted_scores)

for i in range(len(sorted_scores)):
    print(f'第{i + 1}名：{sorted_scores[i][0]}，成绩为{sorted_scores[i][1]}分')