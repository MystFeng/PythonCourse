with open("miku", "r", encoding="utf8") as file:
    for i in file:
        if not i.startswith('#'):
            print(i.strip())