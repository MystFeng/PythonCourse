class Course:
    def __init__(self, number, name, teacher, location):
        self.number = number
        self.name = name
        self.teacher = teacher
        self.__location = location  # 使用双下划线将location设为私有属性

    def show_info(self):
        print(f"课程编号: {self.number}")
        print(f"课程名称: {self.name}")
        print(f"任课教师: {self.teacher}")
        print(f"上课地点: {self.__location}")


# 创建一个课程对象
my_course = Course("C101", "Python Programming", "Dr. Smith", "Room 201")

# 尝试直接访问私有属性（会报错）
# print(my_course.__location)

# 调用show_info方法显示课程信息
my_course.show_info()