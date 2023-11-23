def num_sort(file):
    num_li = []
    with open(file, 'r', encoding='utf8') as file:
        for line in file:
            nums = line.strip().split()
            num_li.extend(map(int, nums))
    num_li.sort()
    return num_li


sorted_numbers = num_sort('num')
print(*sorted_numbers, sep="\n")