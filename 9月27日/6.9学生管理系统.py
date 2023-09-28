"""
使用自定义的函数，完成对程序的模块化
学生信息包含：姓名、性别、手机号，参考格式如下：
[{"name":"张三","sex":"男","phone":123456},{"name":"李四","sex":"男","phone":654321}]
该系统具有的功能：添加、删除、修改、显示、退出系统
设计思路：
提示用户选择功操作
获取用户选择的功能
根据用户的选择，分别调用不同的函数
"""

# 存储学生信息列表
students = [
    {'name': '张三', 'phone': '12345', 'sex': '女'},
    {'name': '李四', 'phone': '67890', 'sex': '男'},
    {'name': '蔡徐坤', 'phone': '110', 'sex': '鸡你太美'},
    {'name': 'vansama', 'phone': '114514', 'sex': '基佬'}
]


def print_stu_info(student):
    print(f"姓名：{student['name']}，电话：{student['phone']}，性别：{student['sex']}")


def print_menu():
    print(
        '————————————————\n'
        '学生管理系统 V10.0\n'
        '1.添加学生信息\n'
        '2.删除学生信息\n'
        '3.修改学生信息\n'
        '4.查询所有学生信息\n'
        '0.退出系统\n'
    )


def add_stu_info():
    new_student = {
        'name': input('请输入学生姓名: '),
        'phone': input('请输入学生ID: '),
        'sex': input('请输入学生性别（男/女）: ')
    }
    students.append(new_student)
    print('已添加。')


def del_stu_info():
    del_student_name = input('要删除哪位学生（姓名）？')
    for student in list(students):
        if student['name'] == del_student_name:
            students.remove(student)
            print(f'已经删除{del_student_name}。')
            break
    else:
        print('找不到这名学生。')


def mod_stu_info():
    mod_student_name = input('要修改哪位学生（姓名）？')
    for student in students:
        if student['name'] == mod_student_name:
            print('找到了学生信息：')
            print_stu_info(student)
            mod_type = input('请问要修改什么信息(name姓名/phone电话/sex性别)？')
            new_value = input('请输入新的值：')
            student[mod_type] = new_value
            print('学生信息已更新：')
            print_stu_info(student)
            break
    else:
        print('找不到这名学生。')


def show_stu_info():
    if not students:
        print('学生列表为空。')
    else:
        print('学生信息如下：')
        for student in students:
            print_stu_info(student)


def main():
    while True:
        print_menu()
        key = input("请输入功能对应的数字：")
        # 添加学生信息
        if key == '1':
            add_stu_info()
        # 删除学生信息
        elif key == '2':
            del_stu_info()
        # 修改学生信息
        elif key == '3':
            mod_stu_info()
        # 查询所有学生信息
        elif key == '4':
            show_stu_info()
        # 退出系统
        elif key == '0':
            quit_confirm = input('确实要退出吗(Y/N)？').lower()
            if quit_confirm == 'y':
                print("再见!")
                break
            elif quit_confirm == 'n':
                continue
            else:
                print('输入错误。')


if __name__ == '__main__':
    main()