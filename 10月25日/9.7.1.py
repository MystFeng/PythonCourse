import math


def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("半径不能为负值")
    else:
        return math.pi * (radius ** 2)


try:
    radius = float(input("请输入圆的半径："))
    area = calculate_circle_area(radius)
    print(f"圆的面积为：{area}")

except ValueError as e:
    print(f"错误：{e}")