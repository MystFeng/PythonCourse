def count_alphabet(str):
    count = {}
    for char in str:
        if char in count.keys():
            count[char] += 1
        else:
            count[char] = 1
    print(count)


str = 'skdaskerkjsalkj'

if __name__ == "__main__":
    count_alphabet(str)

