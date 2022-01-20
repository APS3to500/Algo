# 시간초과

def solution(brown, yellow):
    total = brown + yellow
    for sero in range(1, total+1):
        for garo in range(sero, total+1):
            if garo * sero == total and (garo + sero - 2) * 2 == brown:
                return [garo, sero]