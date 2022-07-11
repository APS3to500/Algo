import heapq

n = int(input())
heap = []
for _ in range(n):
    d, w = map(int, input().split())
    heapq.heappush(heap, (-d, w))

left = heap[0][0]

score = 0
work = []
while left < 0:

    while heap and heap[0][0] == left:
        d, w = heapq.heappop(heap)
        heapq.heappush(work, -w)

    left += 1
    if work:
        score -= heapq.heappop(work)

print(score)
