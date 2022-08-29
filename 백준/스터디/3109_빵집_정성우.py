R, C = map(int, input().split())

dr = [-1, 0, 1]
dc = [1, 1, 1]

graph = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

cnt = 0


def dfs(r, c):
    global cnt, flag
    if c == C - 1:
        cnt += 1
        flag = True
        return

    for i in range(3):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] == '.':
            graph[nr][nc] = 'x'
            dfs(nr, nc)

        if flag:
            return


for k in range(R):
    if graph[k][0] == '.':
        flag = False
        dfs(k, 0)
print(cnt)