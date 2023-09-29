import time

total_count = 50
print('=' * (total_count - 1) + '开始下载' + '=' * (total_count - 1))
for i in range(total_count + 1):
    completed = "*" * i
    incomplete = "." * (total_count - i)
    percentage = (i / total_count) * 100
    print("\r{:.0f}%[{}{}]".format(percentage, completed, incomplete), end="")
    time.sleep(0.5)
print("\n" + '=' * (total_count - 1) + '下载完成' + '=' * (total_count - 1))