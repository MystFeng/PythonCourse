while True:
    print("选择操作：\n1.加法\n2.减法\n3.乘法\n4.除法\n5.退出")
    choice = input("请输入你的选项：")
    if choice == '5':
        print("退出程序。")
        break
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    if choice == '1':
        print(num1 + "加" + num2 + "的结果是" + (num1 + num2))
    elif choice == '2':
        print(num1 + "减" + num2 + "的结果是" + (num1 - num2))
    elif choice == '3':
        print(num1 + "乘" + num2 + "的结果是" + (num1 * num2))
    elif choice == '4':
        if num2 == 0:
            print("除数不为0")
        else:
            print("结果：", num1 / num2)
    else:
        print("无效的输入")
