def update_info(info):
    for i in info:
        if i.keys() == 1:
            info.pop(i.value())


if __name__ == "__main__":
    sinfo = {"xiaohong": 0, "xiaolan": 0, "xiaoming": 1, "xiaobai": 1}
    print(f"修改前：{sinfo}")
    update_info(sinfo)
    print(f"修改后：{sinfo}")
