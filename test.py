import random

pistol_magazine = [0, 0, 0, 0, 0, 0]  # 弹夹

print("你想赌几颗子弹？")
bet = int(input())
if 0 <= bet <= 6:
    for i in random.sample(range(len(pistol_magazine)), bet):
        pistol_magazine[i] = 1
else:
    print("\"滚！\"，庄家啐了我一脸酒。似乎我开了一个程序员才能理解的玩笑，可惜在这里并不好笑。")

print(pistol_magazine)