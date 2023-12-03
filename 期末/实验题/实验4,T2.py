def update_info(sinfo):
    for name, gender in list(sinfo.items()):
        sinfo.pop(name) if gender == 1 else None
    return sinfo


if __name__ == "__main__":
    sinfo = {"xiaohong": 0, "xiaolan": 0, "xiaoming": 1, "xiaobai": 1}
    print(f"修改前的信息:{sinfo}")
    sinfo = update_info(sinfo)
    print(f"修改后的信息:{sinfo}")