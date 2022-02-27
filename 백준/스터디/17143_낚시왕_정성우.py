import sys

input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

R, C, M = map(int, input().split())
graph = [[0] * C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    if d == 1 or d == 2:
        s %= (R - 1) * 2
    else:
        s %= (C - 1) * 2
    graph[r - 1][c - 1] = (s, d - 1, z)
answer = 0
for i in range(C):
    for j in range(R):
        if graph[j][i]:
            answer += graph[j][i][2]
            graph[j][i] = 0
            break

    temp = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if graph[x][y]:
                r, c = x, y
                s, d, z = graph[x][y]
                # 개선 가능해보이지만 포기...
                while s > 0:
                    nr, nc = r + dr[d], c + dc[d]
                    s -= 1
                    if nr >= R:  # 아래 초과
                        d = 0
                        nr -= 2
                    elif nr < 0:  # 위 초과
                        d = 1
                        nr += 2
                    elif nc >= C:  # 오른쪽 초과
                        d = 3
                        nc -= 2
                    elif nc < 0:  # 왼쪽 초과
                        d = 2
                        nc += 2
                    r, c = nr, nc
                if temp[r][c]:
                    if temp[r][c][2] > z:
                        continue

                temp[r][c] = (graph[x][y][0], d, z)
    graph = temp
print(answer)
