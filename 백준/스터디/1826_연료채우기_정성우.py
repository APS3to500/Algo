import heapq
import sys

input = sys.stdin.readline

n = int(input())

cnt = 0
min_heap = []
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(min_heap, (a, b))
target, fuel = map(int, input().split())

max_heap = []
while fuel < target:

    while min_heap and min_heap[0][0] <= fuel:
        a, b = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-b, a))

    if not max_heap:
        cnt = -1
        break

    cnt += 1
    b, a = heapq.heappop(max_heap)
    fuel -= b

print(cnt)
