s = 'skdaskerkjsalkj'
d1 = {}
for elem in s:
    if elem in d1.keys():
        d1[elem] += 1
    else:
        d1[elem] = 1
# 简化版
# for elem in s:
#     d1[elem] = d1.get(elem, 0) + 1

for key, value in d1.items():
    print(f"{key}:{value}")