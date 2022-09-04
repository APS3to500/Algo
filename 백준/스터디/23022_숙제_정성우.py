from heapq import heappop, heappush
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s = map(int, input().split())
    t = list(map(int, input().split()))
    v = list(map(int, input().split()))

    ans = 0

    q = []
    for i in range(n):
        heappush(q, (t[i], v[i]))
    maxheap = []
    while q or maxheap:
        while q and q[0][0] <= s:
            a, b = heappop(q)
            heappush(maxheap, (-b, a))
        if maxheap:
            c, d = heappop(maxheap)
            ans += (s - d) * (-c)
        # 1 단위 시간 뒤에 풀 숙제가 없다면 즉시 이동
        if q and q[0][0] > s and not maxheap:
            s = q[0][0]
        else:
            s += 1

    print(ans)
