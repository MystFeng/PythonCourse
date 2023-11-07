def file_read(file):
    file = open(file, "r", encoding="utf8")
    file_data = []
    for line in file:
        if not line.startswith('#'):
            file_data.append(line.strip())
    return file_data


data_lines = file_read("miku.txt")
print(*data_lines, sep='\n')