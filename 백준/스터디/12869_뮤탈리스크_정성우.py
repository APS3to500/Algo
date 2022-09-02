from collections import deque
from itertools import permutations

inf = int(1e9)
dp = [[[inf] * 61 for _ in range(61)] for _ in range(61)]

n = int(input())
scv = list(map(int, input().split()))

for _ in range(3 - len(scv)):
    scv.append(0)
perm = list(permutations(scv, 3))
q = deque()

for a, b, c in perm:
    q.append((a, b, c, 0))

while q:
    first, second, third, cnt = q.popleft()
    if first == second == third == 0:
        print(cnt)
        break

    first -= 9
    second -= 3
    third -= 1
    cnt += 1
    if first < 0:
        first = 0
    if second < 0:
        second = 0
    if third < 0:
        third = 0
    perm = list(permutations([first, second, third], 3))

    for a, b, c in perm:
        if dp[a][b][c] > cnt:
            dp[a][b][c] = cnt
            q.append((a, b, c, cnt))
