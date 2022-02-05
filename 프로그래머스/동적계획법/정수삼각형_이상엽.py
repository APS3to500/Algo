def solution(triangle):
    start = triangle[0]
    for i in range(1, len(triangle)):
        now = triangle[i]
        sumList = []
        for j in range(len(now)):
            if j == 0:
                tmp = start[j] + now[j]
                sumList.append(tmp)
            elif j == len(now) - 1:
                tmp = start[j-1] + now[j]
                sumList.append(tmp)
            else:
                tmp = max(start[j]+now[j], start[j-1]+now[j])
                sumList.append(tmp)
        start = sumList
    answer = max(sumList)
    return answer