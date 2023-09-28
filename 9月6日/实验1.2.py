a = 'Hello'
b = '#2#Lisaend'
result = ''
if '#2#' in b:
    start_index = b.index('#2#') + len('#2#')
    end_index = b.index('end')
    middle_string = b[start_index:end_index]
    result = a + ' ' + middle_string
else:
    result = 'nullnullnull'
print(result)