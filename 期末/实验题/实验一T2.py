a = 'Hello'
b = '#2#Lisaend'
result = ''
if '#2#' in b:
    start = b.index('#2#') + len('#2#')
    end = b.index('end')
    middle = b[start:end]
    result = a + ' ' + middle
else:
    result = 'null'
print(result)