from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque([(0, 0)])
    while q:
        cursum, idx = q.popleft()

        if idx == len(numbers):
            if cursum == target:
                answer += 1

        else:
            q.append((cursum - numbers[idx], idx + 1))
            q.append((cursum + numbers[idx], idx + 1))
    return answer
