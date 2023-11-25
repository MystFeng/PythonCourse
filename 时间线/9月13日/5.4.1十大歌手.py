def calculate_average_score(scores):
    trimmed_scores = sorted(scores)[1:-1]
    print(trimmed_scores)
    average_score = sum(trimmed_scores) / len(trimmed_scores)
    return average_score


def get_scores():
    scores = []
    for i in range(10):
        scores.append(float(input(f"请输入第{i + 1}位评委的打分：")))
    return scores


def main():
    average_score = calculate_average_score(get_scores())
    print(f"该选手的最终得分是：{average_score}")


if __name__ == "__main__":
    main()