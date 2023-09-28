from 9月27日.6.9学生管理系统 import add_stu_info, del_stu_info, mod_stu_info, print_menu, show_stu_info


str = 'ppssAQWssd'


def count(str):
    upper_count = 0
    lower_count = 0
    for char in str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return (upper_count, lower_count)


if __name__ == "__main__":
    result = count(str)
    print(result)


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