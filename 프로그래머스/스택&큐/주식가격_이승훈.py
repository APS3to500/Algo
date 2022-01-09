from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        price = prices.popleft()
        sec=0
        for nex in prices:
            if price>nex:
                sec+=1
                break
            else:
                sec+=1
        answer.append(sec)
    return answer