from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        time = 0
        tmp = prices.popleft()
        for price in prices:
            if price >= tmp:
                time += 1
            else:
                time += 1
                break
        answer.append(time)
    return answer