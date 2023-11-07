import os

filename = input("输入文件名称：")
allowed_formats = ['.jpg', '.jpeg', '.png']


def check_avatar_format(name):
    file_format = os.path.splitext(name)[-1].lower()
    if file_format not in allowed_formats:
        raise Exception(f"格式错误：只允许上传{' '.join(allowed_formats)}格式的文件")
    return f"{name}格式正确!"


try:
    result = check_avatar_format(filename)
    print(result)
except Exception as e:
    print(e)