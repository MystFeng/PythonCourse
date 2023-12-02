class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14 * self.r * self.r

    def get_perimeter(self):
        return 2 * 3.14 * self.r


c = Circle(2)
print(c.get_area(), c.get_perimeter())