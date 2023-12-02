try:
    radius = float(input("请输入圆的半径："))
    if radius < 0:
        raise ValueError("半径不能为负值")
    else:
        area = 3.14 * (radius ** 2)
        print(f"圆的面积为：{area}")
except ValueError as e:
    print(f"错误：{e}")