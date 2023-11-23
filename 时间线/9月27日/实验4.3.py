def count(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count


if __name__ == "__main__":
    str = 'ppssAQWssd'
    # str = input('输入任意字母串')
    result = count(str)
    print(result)