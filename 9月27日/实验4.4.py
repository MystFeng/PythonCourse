def input_nums():
    counter = 1
    numbers = []
    while True:
        user_input = input(f'请输入第{counter}个实数（输入q结束）：')
        if user_input == 'q':
            break
        numbers.append(float(user_input))
        counter += 1
    return numbers


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
    numbers = input_nums()
    result = handle_nums(numbers)
    print(result)