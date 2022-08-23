def solution(survey, choices):
    answer = ''

    types = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for surv, choice in zip(survey, choices):
        disagree, agree = surv[0], surv[1]

        if choice == 4:
            continue

        if choice > 4:
            types[agree] += choice - 4
        else:
            types[disagree] += 4 - choice

    if types["R"] >= types["T"]:
        answer += "R"
    else:
        answer += "T"

    if types["C"] >= types["F"]:
        answer += "C"
    else:
        answer += "F"

    if types["J"] >= types["M"]:
        answer += "J"
    else:
        answer += "M"

    if types["A"] >= types["N"]:
        answer += "A"
    else:
        answer += "N"
    return answer
