with open('num', 'r', encoding='utf8') as file:
    numbers = [int(num) for line in file for num in line.split()]
    sorted_numbers = sorted(numbers)
print(sorted_numbers)