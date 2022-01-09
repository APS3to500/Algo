def solution(progresses, speeds):
    idx = 0
    answer = []
    while True:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        cnt = 0
        if progresses[idx] < 100:
            continue
        else:
            cnt += 1
            idx += 1
            while True:
                if idx >= len(progresses):
                    answer.append(cnt)
                    return answer
                if progresses[idx] < 100:
                    break
                else:
                    idx += 1
                    cnt += 1
            answer.append(cnt)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))
