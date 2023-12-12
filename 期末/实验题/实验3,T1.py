# 用户输入月份，判断这个月是哪个季节。
# 3、4、5月----春季，6、7、8----夏季，9、10、11---秋季，12、1、2----冬季

# 用字典的方式
# seasons = {'春季': [3, 4, 5],
#            '夏季': [6, 7, 8],
#            '秋季': [9, 10, 11],
#            '冬季': [12, 1, 2]}
#
# input_month = int(input('输入要判断的月份：'))
# for season, months in seasons.items():
#     if input_month in months:
#         print(f'这个月份是{season}')
#         break
# else:
#     print('输入错误！')

# 用if-elif-else语句
input_month = int(input('输入要判断的月份：'))
if input_month in {3, 4, 5}:
    print('这个月份是春季')
elif input_month in {6, 7, 8}:
    print('这个月份是夏季')
elif input_month in {9, 10, 11}:
    print('这个月份是秋季')
elif input_month in {12, 1, 2}:
    print('这个月份是冬季')
else:
    print('输入错误！')