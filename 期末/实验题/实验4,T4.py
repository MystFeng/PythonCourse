def input_nums():
    counter = 1
    numbers_list = []
    while True:
        user_input = input(f'请输入第{counter}个数：')
        if not user_input.isdigit():
            if user_input.lower() == 'q':
                if not numbers_list:
                    print("你还没有输入任何数字。")
                else:
                    break
            else:
                print('须输入有效数字。')
        else:
            numbers_list.append(float(user_input))
            counter += 1
            print(f"已添加{user_input}。")
    return numbers_list


def handle_nums(nums):
    updated_nums = []
    average_num = sum(nums) / len(nums)
    updated_nums.append(average_num)
    for i in nums:
        if i > average_num:
            updated_nums.append(i)
    updated_nums.sort()
    return updated_nums


if __name__ == "__main__":
    print('（开始处理一组实数，输出其平均值和大于平均值的数，输入q开始计算）')
    raw = input_nums()
    result = handle_nums(raw)
    print(f"全部结果：{raw}")
    print(f"最终结果：{result}")