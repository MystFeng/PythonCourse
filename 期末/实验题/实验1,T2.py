a = 'Hello'
b = '#2#Lisaend'

if '#2#' in b:
    start = b.index('#2#') + len('#2#')
    end = b.index('end')
    middle = b[start:end]
    result = a + ' ' + middle
    print(result)
else:
    result = 'null'
# index方法是用来检测元素在变量中首次出现时的位置。