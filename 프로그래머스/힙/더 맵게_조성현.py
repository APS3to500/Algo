# def solution(scoville, K):
#     answer = 0
#     scoville.sort()
#     while True:
#         if scoville[0] >= K:
#             return answer
#         answer += 1
#         a = scoville.pop(0)
#         b = scoville.pop(0)
#         scoville.append(a + b * 2)
#         scoville.sort()
#
#     return answer
import heapq


def solution(scoville, K):
    heap = []
    answer = 0
    for i in scoville:
        heapq.heappush(heap,i)
    while True:
        if heap[0] >= K:
            return answer
        if len(heap) < 2:
            answer = -1
            return answer
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        if a ==0 and b == 0:
            answer = -1
            return answer
        heapq.heappush(heap, a+b*2)
        answer += 1
    return answer

scoville = [0, 0, 3, 9, 10, 12]
K = 7

print(solution(scoville,K))