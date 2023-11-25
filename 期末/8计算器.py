def calculate(x, y, operator):
    operations = {
        "+": x + y,
        "-": x - y,
        "*": x * y,
        "/": x / y if y != 0 else print("除数不能为0")
    }
    return operations[operator] if operator in operations else print("运算符错误")


while True:
    n1 = float(input("请输入第一个数字："))
    n2 = float(input("请输入第二个数字："))
    operator = input("请选择运算符 (+, -, *, /): ")
    result = calculate(n1, n2, operator)
    print("结果：", result)