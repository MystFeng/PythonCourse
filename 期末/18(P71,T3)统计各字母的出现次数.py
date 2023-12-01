str = 'skdaskerkjsalkj'
result = {}
for i in str:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(result)

# 这是美化的写法
# for key, value in result.items():
#     print(f"{key}: {value}", end=', ')