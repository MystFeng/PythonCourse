def calculate_score(scores):
    sorted_scores = sorted(scores)
    trimmed_scores = sorted_scores[1:-1]
    average_score = sum(trimmed_scores) / len(trimmed_scores)
    return average_score


def get_judge_scores():
    scores = []
    for i in range(10):
        scores.append(float(input(f"请输入第{i + 1}位评委的打分：")))
    return scores


def main():
    average_score = calculate_score(get_judge_scores())
    print(f"该选手的最终得分是：{average_score}")


if __name__ == "__main__":
    main()
