import random

z = 0
data1 = random.randint(1, 6)  # 模拟子弹随机到的弹仓
data2 = random.randint(1, 6)  # 模拟撞针旋转到的位置
print(data1)
print(data2)

print(f'子弹在第{data1}个弹槽')
print(f'撞针从第{data2}个弹槽开始打')
while z <= 6:  # 最多开六枪游戏结束
    e1 = input('甲方请开枪:')
    if data2 == data1:
        print('甲方中枪\n游戏结束！')
        break
    else:
        data2 = data2 + 1
        if data2 > 6:  # 如果撞针到最后一个弹仓重新循环
            data2 = 1
        e2 = input('乙方请开枪:')
        if data2 == data1:
            print('乙方中枪\n游戏结束！')
            break
        else:
            data2 = data2 + 1
            if data2 > 6:  # 如果撞针到最后一个弹仓重新循环
                data2 = 1
    z += 1