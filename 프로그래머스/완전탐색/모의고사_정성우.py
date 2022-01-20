def solution(answers):
    answer = []

    giveup1 = [1, 2, 3, 4, 5] * 2000
    giveup2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    giveup3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    match = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == giveup1[i]:
            match[0] += 1
        if answers[i] == giveup2[i]:
            match[1] += 1
        if answers[i] == giveup3[i]:
            match[2] += 1

    for i, v in enumerate(match):
        if v == max(match):
            answer.append(i + 1)

    return answer
