def solution(clothes):
    answer = 1
    comb = {}
    for i in range(len(clothes)):
        comb[clothes[i][1]] = 0
    for i in range(len(clothes)):
        comb[clothes[i][1]] += 1

    val = list(comb.values())
    
    for j in range(len(val)):
        answer *= val[j] + 1
    return answer - 1