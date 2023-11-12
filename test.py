import random

pistol_magazine = [0, 0, 0, 0, 0, 0]  # 弹夹
bet = 1
for i in random.sample(range(len(pistol_magazine)), bet):
    pistol_magazine[i] = 1
print(pistol_magazine)