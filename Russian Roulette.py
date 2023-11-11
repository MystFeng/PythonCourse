import random
import time

characters = {
    '庄家': {
        'title': "桌子对面的",
        'default': "庄家看着你，冷冷地说：\"再玩一把吗？\"",
        'contingency': "",
        'win': "庄家笑着说：\"你真是个幸运儿！\"",
        'lose': "庄家嘲讽地说：\"运气不太好啊！\"",
    },
    '修女': {
        'title': "看似善良的",
        'default': "修女微笑着对你说：\"愿神与你同在。\"",
        'contingency': "",
        'win': "修女感叹道：\"神一定在庇佑着你！\"",
        'lose': "修女安慰你说：\"有时候运气就是这样。\"",
    },
    '老奶奶': {
        'title': "想找人给她洗洗脚的",
        'default': "老奶奶神秘地笑着：\"生活就像一盒巧克力，你永远不知道下一颗是什么味道。\"",
        'contingency': "老奶奶在洗脚的时候，不经意地碰到了枪。\n你发现枪稍微移动了一下，但你决定什么也不说。",
        'win': "老奶奶高兴地说：\"看来神听到了我的祈祷！\"",
        'lose': "老奶奶叹了口气：\"运气不太好啊，年轻人。\"",
    },
}  # 游戏角色

game_round = 0  # 回合数
loader = 0  # 装弹者
wager = 0  # 赌注
money = 100  # 金钱
winnings = 0  # 赢钱
pistol_magazine = [0, 0, 0, 0, 0, 0]  # 弹夹

firing_probability = 1.00  # 手枪击发概率
additional_behavior_probability = 0.00  # 意外事件概率
consequence_probability = 0.00  # 击发后果概率


def load():
    global pistol_magazine
    print("你想赌几颗子弹？")
    bet = int(input())
    if 0 <= bet <= 6:
        for i in random.sample(range(len(pistol_magazine)), bet):
            pistol_magazine[i] = 1
        print(f"{loader}装入了子弹，然后把枪放到你的手上。")
    else:
        print("\"滚！\"，庄家啐了我一脸酒。似乎我开了一个程序员才能理解的玩笑，可惜在这里并不好笑。")
        return load()


def choose_loader():
    global loader
    time.sleep(0.5)
    print("你看中了酒馆里的一个人，祂就是：")
    for i, person in enumerate(characters.keys()):
        print(f"{i + 1}. {characters[person]['title']}{person}")
    time.sleep(0.5)
    choose = int(input("...会是谁呢？")) - 1
    if list(characters.keys())[choose] is None:
        time.sleep(0.5)
        print(f"我总在回忆{choose}这个号码，却发现它是子虚乌有。选错了！F**k...\n")
        return choose_loader()
    else:
        loader = list(characters.keys())[choose]
        print(f"{loader}会帮你装弹...")


def russian_roulette(player_type, bet, additional_behavior_probability, consequence_probability):
    if player_type == "老奶奶":
        print("")
        time.sleep(1)

    for _ in range(6):
        input("按下回车装弹...")
        pulled_trigger = random.choice(magazine)

        if pulled_trigger == 1:
            print("砰！子弹击中了！")
            if player_type == "修女" and random.random() < consequence_probability:
                print("但是由于奇迹般的幸运，你只是受了点轻伤！")
            return bet * 2  # 返回赢得的奖金
        print("枪没有响，你感觉到了一丝安全。")
    print("所有的弹膛都被扣动了，但是没有发生任何事情。")
    return 0  # 返回赌注


def check_cash():
    if money > 0:
        print(f"现在有{money}元。")
    elif money == 0:
        print(f"现在没钱了。")
    elif money < 0:
        print(f"还欠{abs(money)}元。")


def main():
    check_cash()

    # time.sleep(0.5)
    # print("我该装子弹了...")
    # time.sleep(1)
    # print("好醉啊！得找人给我装子弹...")
    choose_loader()
    load()

    time.sleep(2)
    winnings = russian_roulette(loader, bet, additional_behavior_probability, consequence_probability)
    money += winnings
    print(f"\n你 {'赚取了' if winnings > 0 else '失去了'} {abs(winnings)} 金币。")


def story():
    #     time.sleep(0.5)
    #     print("我是个酒鬼，日复一日地在酒馆里碌碌无为。")
    #     time.sleep(2)
    #     print("酒馆里昏暗的灯光勉强照亮了角落，桌上散乱的杯具和破旧的扑克牌散发着难闻的味道。")
    #     time.sleep(2)
    #     print("我在一张酒味浓郁的桌上醉倒，没有注意到一个正在寻欢作乐的人坐到我的旁边。")
    #     time.sleep(2)
    #     print("...")
    #     time.sleep(2)
    #     print("......")
    #     time.sleep(2)
    #     print("\"黄金！\"我抬头，看到了与我无缘的东西...")
    #     time.sleep(2)
    #     print("好多黄金...而在黄金的背后是一个戴着帽子的家伙。我知道是他叫醒了我，因为他在我旁边开了一枪。")
    #     time.sleep(2)
    #     print("但这些并不重要。重要的是，那个人居然有黄金！")
    #     time.sleep(2)
    #     print("\"朋友，吃一枪吧！\"桌对面的人向我伸来一把枪。\"还有黄金！\"")
    #     time.sleep(2)
    #     print("我...拿起了枪。")
    #     time.sleep(2)
    pass


if __name__ == "__main__":
    story()
    main()