import heapq
import sys

input = sys.stdin.readline
n, k = map(int, input().split())

jewel = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewel, (m, v))
ans = 0
bags = []
for _ in range(k):
    bags.append(int(input()))

bags.sort()
heap = []
for bag in bags:
    while jewel and bag >= jewel[0][0]:
        m, v = heapq.heappop(jewel)
        heapq.heappush(heap, -v)

    if heap:
        ans -= heapq.heappop(heap)

print(ans)
