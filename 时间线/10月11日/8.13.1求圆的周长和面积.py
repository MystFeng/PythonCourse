class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return 2 * 3.14 * self.radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)


# 创建一个半径为5的圆对象
my_circle = Circle(5)

# 求圆的周长和面积
perimeter = my_circle.get_perimeter()
area = my_circle.get_area()

print(f"圆的周长为: {perimeter:.2f},面积为: {area}")