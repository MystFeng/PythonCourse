import random
import time

pistol_magazine = [0, 0, 0, 0, 0, 0]
game_rounds = 0
firing_probability = 1
people_in_bar = {
    1: '你的庄家',
    2: '看似善良的修女',
    3: '迫不及待想洗脚的老奶奶',
}


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


def load_magazine():
    pass


def load():
    print("我该装子弹了...或者我可以找别人来为我装弹。")
    bet_bullets = int(input("你想赌几颗子弹呢？"))
    if bet_bullets < 0 or bet_bullets > 6:
        print("\"滚！\"，庄家啐了我一脸酒。似乎我开了一个程序员才能理解的玩笑，可惜在这里并不好笑。")
        return load()
    else:
        random_indices = random.sample(range(len(pistol_magazine)), bet_bullets)
        for index in random_indices:
            pistol_magazine[index] = 1
        print()


def choose_loader():
    print("你看中了酒馆里的一个人，他/她就是：")

    for index, person in people_in_bar.items():
        print(f"{index}. {person}")

    choice = int(input())

    loader = people_in_bar.get(choice)
    if loader is None:
        print(
            "有这号人吗？你仰起酸胀的脖子，回忆了一下前世的记忆。\n"
            "然后你发现你他娘的根本就没有前世的记忆！\n看来你得重新选了。")
        return choose_loader()
    return loader


def russian_roulette(player_type, bet, additional_behavior_probability, consequence_probability):
    if player_type == "老奶奶":
        print("老奶奶在洗脚的时候，不经意地碰到了枪。")
        print("你发现枪稍微移动了一下，但你决定什么也不说。")
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


def main():
    money = 100  # 初始金钱
    if money > 0:
        print(f"现在有{money}元。")
    elif money == 0:
        print("现在没钱了。")
    elif money < 0:
        print(f"还欠{abs(money)}元。")

    bet = load()
    loader = choose_loader()
    additional_behavior_probability = 0.00
    consequence_probability = 0.00

    print(f"{loader}会帮你装弹...")
    time.sleep(2)

    winnings = russian_roulette(loader, bet, additional_behavior_probability, consequence_probability)

    money += winnings
    print(f"\n你 {'赚取了' if winnings > 0 else '失去了'} {abs(winnings)} 金币。")


if __name__ == "__main__":
    story()
    main()