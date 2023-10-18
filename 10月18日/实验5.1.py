# 定义一个类people，拥有name，age两个公有属性，weight一个私有属性。定义构造方法进行初始化，定义speak方法，输出name，age，weight。
# 定义一个类student，继承自people。拥有grade公有属性。
# 定义student的构造方法进行初始化，定义speak方法，输出grade。
# 定义student类的对象，调用speak输出name，age，weight，grade。
class people:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print(f"name:{self.name}, age:{self.age}, weight:{self.__weight}")


class student(people):
    def __init__(self, name, age, weight, grade):
        super().__init__(name, age, weight)
        self.grade = grade

    def speak(self):
        super().speak()
        print(f"grade:{self.grade}")


# Jack = student("Jack", 30, 70, 100)
# Jack.speak()


# 在以上两个类people和student的基础上，再定义一个类singer，不继承自任何类。此类拥有自己的公有属性song。
# 定义构造方法进行初始化，定义speak方法，输出song。

# 定义一个类sample，多重继承自student和singer。定义sample的构造函数进行初始化。
# 定义sample的对象，调用speak输出name，age，weight，grade，song。
class singer:
    def __init__(self, song):
        self.song = song

    def speak(self):
        print(f"song:{self.song}")


class sample(student, singer):
    def __init__(self, name, age, weight, grade, song):
        student.__init__(self, name, age, weight, grade)
        singer.__init__(self, song)

    def speak(self):
        student.speak(self)
        singer.speak(self)


Amy = sample("Amy", 25, 65, 90, "Good Song")
Amy.speak()