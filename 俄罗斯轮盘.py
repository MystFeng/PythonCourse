import random
import time


class Pistol:
    magazine = [0, 0, 0, 0, 0, 0]
    game_rounds = 0
    firing_probability = 1


def place_bet():
    print("\"该上子弹了...或者找别人为你装弹。")
    num_bullets = int(input("你想赌几颗子弹呢？"))
    if num_bullets < 0 or num_bullets > 6:
        print("\"滚！\"，庄家啐了你一脸酒。")
        return place_bet()
    return num_bullets


def choose_loader():
    print("你看中了酒馆里的一个人，他/她就是：")

    people_in_bar = {
        1: '你的庄家',
        2: '看似善良的修女',
        3: '迫不及待想洗脚的老奶奶',
        4: '威猛的猎人',
        5: '调皮的雌小鬼',
        6: '对雌小鬼满脸堆笑的杂鱼大叔',
        7: '被灌醉的小正太',
        8: '正在对小正太上下其手的成熟阿姨',
        9: ''
    }

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
    total_money = 100  # 初始金钱
    if total_money > 0:
        print(f"\n现在有 {total_money} 金币。")
    else:
        print("现在没钱了。")

    bet = place_bet()
    total_money -= bet
    loader = choose_loader()
    additional_behavior_probability = float(input("请输入装弹者的额外行为概率（0 到 1 之间的小数）："))
    consequence_probability = float(input("请输入额外行为导致的后果概率（0 到 1 之间的小数）："))

    print(f"你选择让{loader} 帮你装弹...")
    if loader == "老奶奶" and random.random() < additional_behavior_probability:
        print("老奶奶往枪里抹了一些胶，增加了卡壳概率！")
        magazine.append(0)  # 增加一个没有子弹的弹膛

    time.sleep(2)

    if bet < 2 and loader == "修女" and random.random() < additional_behavior_probability:
        print("修女双手抱握，正在为你祈祷。")
    elif bet >= 5 and loader == "猎人" and random.random() < additional_behavior_probability:
        print("猎人猛拍桌子，放声大笑，酒沫从嘴里喷到胡子上。")

    winnings = russian_roulette(loader, bet, additional_behavior_probability, consequence_probability)

    total_money += winnings
    print(f"\n你 {'赚取了' if winnings > 0 else '痛失'} {abs(winnings)} 金币。")


if __name__ == "__main__":
    time.sleep(0.5)
    print("我是个酒鬼，日复一日地在酒馆里碌碌无为")
    time.sleep(1)
    print("酒馆里昏暗的灯光勉强照亮了角落，桌上散乱的杯具和破旧的扑克牌散发着难闻的味道")
    time.sleep(1)
    print("酒味浓郁，让人不禁觉得在这里花朵会被烈酒泡发，黄金也会被烈酒融化")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("\"黄金！\"我抬头，看到了本与我无缘的东西...")
    time.sleep(1)
    print("好多黄金...而在黄金的背后是一个戴着帽子的家伙。我对那个人没有兴趣")
    time.sleep(1)
    print("更重要的是那个人真的有黄金！而且...他是不是还有把手枪啊？")
    time.sleep(1)
    print("\"朋友，请你...吃一枪怎么样？\"桌对面的人向我伸来一把枪\n")
    time.sleep(1)
    print("他把枪里的子弹拔出，然后一并交到了我手上。")
    time.sleep(1)
    print("我答应了。")
    time.sleep(1)
    main()