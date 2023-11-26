players = {}
list = []
while True:
    name = input("请输入选手名字(按Q退出)：")
    score = float(input("请输入选手成绩(按Q退出)："))
    if name.lower() == 'q' or score.lower() == 'q':
        break
    players[name] = score

sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
for i, (name, score) in enumerate(sorted_players, 1):
    print(f"第{i}名：{name}，成绩为{score}分")