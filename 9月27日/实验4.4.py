def input_nums():
    counter = 1
    numbers_list = []
    while True:
        user_input = input(f'请输入第{counter}个实数（输入q开始计算）：')
        if user_input.lower() == 'q':
            if not numbers_list:
                print("你还没有输入任何数字。")
            else:
                break
        elif not user_input.isdigit():
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
    updated_nums = tuple(updated_nums)
    return updated_nums


if __name__ == "__main__":
    result = handle_nums(input_nums())
    print(f"最终的结果是：{result}")