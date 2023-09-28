string = "青岛科大欢迎您"
print(string[0:2])
print(string[2:])
print(string[2: len(string) - 1])
new_string = string[-3:] + string[2:4] + string[:2]
print(new_string)