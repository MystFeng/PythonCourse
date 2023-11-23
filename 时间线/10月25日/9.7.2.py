import math


def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return True
    return False


def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


try:
    a = float(input("请输入第一条边："))
    b = float(input("请输入第二条边："))
    c = float(input("请输入第三条边："))

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("边长必须为正数")
    elif not (a + b > c and a + c > b and b + c > a):
        raise ValueError("无法构成任意三角形")
    elif is_right_triangle(a, b, c):
        print(f"可以构成直角三角形！其面积为： {calculate_area(a, b, c)}")
    else:
        print("无法构成直角三角形")

except ValueError as e:
    print(f"错误：{e}")