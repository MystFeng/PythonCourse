# 用户输入月份，判断这个月是哪个季节。
# 3，4，5月----春季  6，7，8----夏季   9，10，11---秋季  12，1，2----冬季

season = {'春季': {3, 4, 5}, '夏季': {6, 7, 8}, '秋季': {9, 10, 11}, '冬季': {12, 1, 2}}
input_month = int(input('输入要判断的月份：'))
for key, value in season.items():
    if input_month in value:
        print(f'这个月份在{key}')
        break
else:
    print('输入错误！')