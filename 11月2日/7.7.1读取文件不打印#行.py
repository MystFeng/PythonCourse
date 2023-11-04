mikulyrics = open("miku.txt", 'r', encoding='utf-8')
for line in mikulyrics:
    if not line.startswith('#'):
        print(line.strip())