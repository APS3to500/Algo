n, m, h = map(int, input().split())
stair = [[0] * n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    stair[a - 1][b - 1] = 1

ans = 5


def go_down():
    flag = False
    for i in range(n):
        r = 0
        c = i
        while True:
            if flag:
                r += 1
                flag = False
                continue
            if r >= h:
                if c == i:
                    break
                else:
                    return False
            else:
                if stair[r][c] == 0 and stair[r][c - 1] == 0:
                    r += 1
                elif stair[r][c] == 1:
                    c += 1
                    flag = True
                elif stair[r][c - 1] == 1:
                    c -= 1
                    flag = True
    return True


def dfs(x, y, k):
    global ans

    if k == 4:
        return

    if go_down():
        ans = min(ans, k)

    for r in range(x, h):
        t = y if r == x else 0  # 매우 중요, 같은 가로줄이면 y부터 확인하고 아니라면 0부터 확인
        for c in range(t, n - 1):
            if not stair[r][c] and not stair[r][c - 1]:
                stair[r][c] = 1
                dfs(r, c, k + 1)
                stair[r][c] = 0


dfs(0, 0, 0)
if ans == 5:
    print(-1)
else:
    print(ans)
