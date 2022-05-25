import heapq
import sys

input = sys.stdin.readline
left = []
right = []

for _ in range(int(input())):
    i = int(input())
    if len(left) == len(right) == 0:
        heapq.heappush(left, (-i, i))
        print(i)
        continue
    if len(left) > len(right):
        if left[0][1] <= i:
            heapq.heappush(right, i)
        else:
            heapq.heappush(right, heapq.heappop(left)[1])
            heapq.heappush(left, (-i, i))
    else:
        if left[0][1] >= i:
            heapq.heappush(left, (-i, i))
        else:
            heapq.heappush(right, i)
            temp = heapq.heappop(right)
            heapq.heappush(left, (-temp, temp))

    print(left[0][1])
