tu_num1 = ('p', 'y', 't', ['o', 'n'])
list_num1 = list(tu_num1)
list_num1[-1].append('h')
tu_num1 = tuple(list_num1)

print(tu_num1)