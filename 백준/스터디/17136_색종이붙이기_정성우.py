dist = [list(map(int, input().split())) for _ in range(10)]

paper = [0, 5, 5, 5, 5, 5]

ans = 987654321


def cover(r, c, size, now):
    # 색종이 붙이기
    for a in range(r, r + size):
        for b in range(c, c + size):
            dist[a][b] = 0
    paper[size] -= 1
    dfs(now + 1)

    # 색종이 떼기
    for a in range(r, r + size):
        for b in range(c, c + size):
            dist[a][b] = 1
    paper[size] += 1


def dfs(now):
    global ans
    if now > ans:
        return

    for i in range(10):
        for j in range(10):
            if dist[i][j]:
                for l in range(1, 6):
                    flag = True
                    if paper[l] > 0 and i + l <= 10 and j + l <= 10:
                        for x in range(i, i + l):
                            for y in range(j, j + l):
                                if dist[x][y] == 0:
                                    flag = False
                                    break
                            if not flag:
                                break
                        if flag:
                            cover(i, j, l, now)
                return


    ans = min(ans, now)


dfs(0)
if ans == 987654321:
    print(-1)
else:
    print(ans)
