class Course:
    def __init__(self, number, name, teacher, location):
        self.number = number
        self.name = name
        self.teacher = teacher
        self.__location = location

    def show_info(self):
        print(self.number, self.name, self.teacher, self.__location)


math = Course(1, "Math", "Amy", "A123")
math.show_info()