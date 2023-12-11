a = float(input("请输入第一个数："))
b = float(input("请输入第二个数："))
cal = input("请选择运算符：+ - * /:")
if cal == '+':
    print(a + b)
elif cal == '-':
    print(a - b)
elif cal == '*':
    print(a * b)
elif cal == '/':
    if b == 0:
        print("除数不能为0")
    else:
        print(a / b)