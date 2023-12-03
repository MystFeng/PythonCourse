topHitters = {
    "Gehrig": {"bats": 8061, "hits": 2721},
    "Ruth": {"bats": 8399, "hits": 2873},
    "Willams": {"bats": 7706, "hits": 2654}
}

# 1. 输出三位棒球手击中球的概率
for player, data in topHitters.items():
    hit_probability = data["hits"] / data["bats"]
    print(f"{player}击中球的概率是{hit_probability:.3f}")

# 2. 输出三位棒球手的平均击中球的次数
total_hits = sum(data["hits"] for data in topHitters.values())
average_hits = total_hits / len(topHitters)
print(f"平均击中球的次数是{average_hits}")

# 3. 输出三位棒球手中击中球次数最多的一位
max_hits = 0
max_hits_player = None
for player, data in topHitters.items():
    if data["hits"] > max_hits:
        max_hits = data["hits"]
        max_hits_player = player
print(f"击中次数最多的球员是：{max_hits_player}，击中次数为：{max_hits}")