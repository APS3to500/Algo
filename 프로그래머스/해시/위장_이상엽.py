def solution(clothes):
    answer = 1
    johab = {}
    
    for item, kind in clothes:
        if kind in johab:
            johab[kind] += 1
        else:
            johab[kind] = 1
    
    for key, val in johab.items():
        answer *= (val+1)
    
    return answer-1