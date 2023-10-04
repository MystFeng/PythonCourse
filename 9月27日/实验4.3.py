str = 'ppssAQWssd'


def count(str):
    upper_count = 0
    lower_count = 0
    for char in str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return tuple(upper_count, lower_count)


if __name__ == "__main__":
    result = count(str)
    print(result)