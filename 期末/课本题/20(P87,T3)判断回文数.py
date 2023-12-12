a = str(input("输入数字判断回文数："))
if a == a[::-1]:
    print("是回文数")
else:
    print("不是回文数")

# tips:
# a[start:end:step]使用了一种切片
# 这里的 start 是开始索引，end 是结束索引（但不包括结束索引的字符），step 是步长（即每次取字符的间隔，默认为1）。
# a[::-1] 这种用法中， start 和 end 都为空，所以默认从头到尾遍历字符串。step 为 -1，表示从后往前取字符，实现了字符串的反转。
# 例如：
# s[2:5] 表示从索引 2 开始到索引 4（不包括索引 5）的字符。
# s[::2] 表示从头到尾每隔一个字符取一个。