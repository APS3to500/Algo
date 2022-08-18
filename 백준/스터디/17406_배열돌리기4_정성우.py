import copy
from itertools import permutations

n, m, k = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(n)]
calc = [list(map(int, input().split())) for _ in range(k)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def turn(r, c, s):
    r -= 1
    c -= 1
    i, j = r - s, c - s
    k = 0
    while s != 0:
        ni = i + di[k]
        nj = j + dj[k]
        if ni > r + s or ni < r - s or nj > c + s or nj < c - s:
            k = (k + 1) % 4
            continue
        arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]
        i = ni
        j = nj
        if ni == r - s and nj == c - s:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            s -= 1
            i += 1
            j += 1


perms = list(permutations(calc, k))
ans = 987654321
for perm in perms:
    arr = copy.deepcopy(temp)
    for r, c, s in perm:
        turn(r, c, s)
    for i in range(n):
        ans = min(ans, sum(arr[i]))

print(ans)
