import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    while scoville[0]<K:
        heapq.heappush(scoville,heapq.heappop(scoville)+2*heapq.heappop(scoville))
    return scoville
solution([1, 2, 3, 9, 10, 12],7)