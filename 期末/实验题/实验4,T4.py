def input_nums():
    counter = 1
    numbers_list = []
    while True:
        user_input = input(f'请输入第{counter}个数：')
        if user_input == "q":
            break
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
    raw_input = input_nums()
    result = handle_nums(raw_input)
    print(f"最终结果：{result}")