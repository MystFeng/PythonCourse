class Student:
    def __init__(self):
        self.stu_info = []

    def print_menu(self):
        print('=' * 30)
        print('学生管理系统 V10.0')
        print('1.添加学生信息')
        print('2.删除学生信息')
        print('3.修改学生信息')
        print('4.查询所有学生信息')
        print('0.退出系统')
        print('=' * 30)

    def add_stu_info(self):
        n = int(input('请输入添加学生人数:'))
        for i in range(n):
            new_name = input(f'请输入第{i + 1}个学生的姓名:')
            new_sex = input(f'请输入第{i + 1}个学生的性别:')
            new_phone = input(f'请输入第{i + 1}个学生的手机号码:')
            new_info = dict()
            new_info['name'] = new_name
            new_info['sex'] = new_sex
            new_info['phone'] = new_phone
            self.stu_info.append(new_info)
            print(f"第{i + 1}个学生信息录入完毕")

    def del_stu_info(self):
        if len(self.stu_info) != 0:
            flag = 0
            name = input('请输入要删除的学生的姓名：')
            for i in range(len(self.stu_info)):
                if self.stu_info[i]["name"] == name:
                    del self.stu_info[i]
                    flag = 1
                    print(f"删除学生姓名为{name}的信息")
                    break
            if flag == 0:
                print("没有找到学生信息")
        else:
            print('学生信息表为空')

    def modify_stu_info(self):
        if len(self.stu_info) != 0:
            name = input('请输入要修改的学生的姓名：')
            flag = 0
            for i in range(len(self.stu_info)):
                if self.stu_info[i]["name"] == name:
                    new_sex = input('请输入要修改学生的性别:(男/女)')
                    new_phone = input('请输入要修改学生的手机号码:')
                    self.stu_info[i]['sex'] = new_sex
                    self.stu_info[i]['phone'] = new_phone
                    flag = 1
                    print("成功修改学生信息")
                    break
            if flag == 0:
                print("未找到对应学生信息")
        else:
            print('学生信息表为空')

    def show_stu_info(self):
        print('学生的信息如下：')
        print('=' * 30)
        print('序号    姓名    性别    手机号码')
        i = 1
        for tempInfo in self.stu_info:
            print("%d    %s    %s    %s" % (i, tempInfo['name'],
                                            tempInfo['sex'], tempInfo['phone']))
            i += 1

    def main(self):
        while True:
            self.print_menu()  # 打印功能菜单
            key = input("请输入功能对应的数字：")
            if key == '1':  # 添加学生信息
                self.add_stu_info()
            elif key == '2':  # 删除学生信息
                self.del_stu_info()
            elif key == '3':  # 修改学生信息
                self.modify_stu_info()
            elif key == '4':  # 查询所有学生信息
                self.show_stu_info()
            elif key == '0':
                quit_confirm = input('亲，真的要退出么？(Yes or No):').lower()
                if quit_confirm == 'yes':
                    print("谢谢使用！")
                    break
                elif quit_confirm == 'no':
                    continue
                else:
                    print('输入有误!')


if __name__ == '__main__':
    student_system = Student()
    student_system.main()