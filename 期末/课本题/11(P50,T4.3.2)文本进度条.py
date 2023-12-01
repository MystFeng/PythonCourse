import time

total_count = 50
bar = '=' * int(total_count / 2)

print(f"\n{bar}开始下载{bar}")
for i in range(total_count + 1):  # 修改为range(total_count + 1)
    complete = "*" * i
    incomplete = "." * (total_count - i)
    percent = (i / total_count) * 100
    print(f"\r{percent:.0f}%[{complete}{incomplete}]", end="")
    time.sleep(0.1)

print(f"\n{bar}下载完成{bar}")