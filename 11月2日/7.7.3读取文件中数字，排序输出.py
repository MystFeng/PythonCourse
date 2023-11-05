newfile = open("number", "r")
numbers = newfile.read()

numbers_list = list(numbers)
numbers_list.sort()
print(numbers_list)