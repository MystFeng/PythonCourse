original = [1, 2, 3, 2, 1, 4, 5, 4, 3]
new = []
# unique = list(set(original))
# print(unique)
for i in original:
    if i not in new:
        new.append(i)
print(new)