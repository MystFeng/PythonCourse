import random
import time

game_round = 0  # 回合

pistol_magazine = [0, 0, 0, 0, 0, 0]  # 弹夹
trigger_shoe = 0  # 扳机位置
shot_count = 0  # 击发数


def load(auto_bet):
    global pistol_magazine
    bet = int(input("要赌几颗子弹？")) if auto_bet is None else random.randint(1, 6)
    if 0 <= bet <= 6:
        for i in random.sample(range(len(pistol_magazine)), bet):
            pistol_magazine[i] = 1
    else:
        print("\"滚。\"，庄家啐了我一脸的酒。")
        print("我是不是装错子弹了...")
        time.sleep(0.5)
        return load(None)
    print(f"我装入了子弹。")
    time.sleep(0.5)


def russian_roulette(auto_toggle):
    time.sleep(0.5)
    global trigger_shoe
    global shot_count
    print(f"我检查了一下弹夹：{pistol_magazine}")
    time.sleep(0.5)
    prod = input("我在思考是否要拨动一下轮子。Y/N:").lower() if auto_toggle is None else random.choice(["y", "n"])

    if prod == "y":
        trigger_shoe = random.randint(0, 5)
        print("手拨弄了一下轮子...随着轮子缓缓停下，我开始默默地祈祷。")
    else:
        print("还是直接来吧，我把枪直接顶到太阳穴上。")
    time.sleep(0.5)
    print("我心跳如鼓，紧握枪柄的手掌中满是汗水，我扣下扳机。")
    time.sleep(2)
    if pistol_magazine[trigger_shoe] == 1:
        pistol_magazine[trigger_shoe] = 0
        shot_count += 1
        print("砰！")
        time.sleep(0.5)
        print("鲜红的好像美酒一样的血从太阳穴喷涌而出，我死了。")
        time.sleep(0.5)
    else:
        print("枪没有响。我感觉到了一丝安全。")
        time.sleep(1)
    print(f"老板走过来检查了一下弹夹：{pistol_magazine}")
    time.sleep(0.5)
    print(f"有{shot_count}发子弹被打出去了...")


def restart():
    global game_round
    response = input("重新开始吗？Y/N:").lower()
    if response == 'y':
        game_round += 1
        print("\n我很不甘心，于是我复活了。\n")
        time.sleep(0.5)
        print("是否快速开始？Y/N:")
        time.sleep(0.5)
        print("Y：替我决定装几发子弹和是否拨动轮子\nN：我自己来")
        quick_start = input().lower()

        if quick_start == 'y':
            main(auto_bet=True, auto_toggle=True)
        else:
            return main(None, None)
    elif response == 'n':
        print("游戏结束。")
    else:
        print("无效的输入。")
        restart()


def clean():
    global pistol_magazine
    global trigger_shoe
    global shot_count

    pistol_magazine = [0, 0, 0, 0, 0, 0]  # 弹夹
    trigger_shoe = 0  #
    shot_count = 0


def main(auto_bet, auto_toggle):
    load(auto_bet)
    russian_roulette(auto_toggle)
    clean()
    restart()


if __name__ == "__main__":
    main(None, None)