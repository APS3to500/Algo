from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    answer = 0
    end = len(q1) + len(q2) + 2

    while sum1 != sum2:
        if sum1 > sum2:
            sum1 -= q1[0]
            sum2 += q1[0]
            q2.append(q1.popleft())
        else:
            sum2 -= q2[0]
            sum1 += q2[0]
            q1.append(q2.popleft())

        answer += 1

        if answer > end:
            return -1

    return answer
