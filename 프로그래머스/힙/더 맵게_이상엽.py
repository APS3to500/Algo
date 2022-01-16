import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # heapq를 리스트화
    
    while scoville[0] < K: # 가장 작은 값이 1번째 값이므로
        if len(scoville) > 1:
            fir = heapq.heappop(scoville)
            sec = heapq.heappop(scoville)
            heapq.heappush(scoville, fir + sec * 2)
            answer += 1
        else:
            return -1
    return answer