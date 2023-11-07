def file_read(file):
    file_data = []
    with open(file, "r", encoding="utf8") as file:
        for line in file:
            if not line.startswith('#'):
                file_data.append(line.strip())
    return file_data


data_lines = file_read("miku")
print(*data_lines, sep="\n")