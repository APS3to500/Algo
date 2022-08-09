from collections import deque
import copy

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

R, C = map(int, input().split())

cave = [list(input()) for _ in range(R)]
n = int(input())
heights = list(map(int, input().split()))


def check(a, b):
    if a >= R or a < 0 or b >= C or b < 0 or cave[a][b] == '.':
        return []
    q = deque()
    q.append((a, b))
    visited = [[0] * C for _ in range(R)]
    visited[a][b] = 1
    temp = [(a, b)]
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr >= R:
                return []
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and cave[nr][nc] == 'x':
                visited[nr][nc] = 1
                q.append((nr, nc))
                temp.append((nr, nc))
    return temp


for i in range(n):
    # 막대기 던지기
    h = heights[i]
    x, y = -h, 0
    if i % 2:
        # 오른쪽
        for j in range(C - 1, -1, -1):
            if cave[-h][j] == 'x':
                cave[-h][j] = '.'
                x, y = R - h, j
                break
    else:
        # 왼쪽
        for j in range(C):
            if cave[-h][j] == 'x':
                cave[-h][j] = '.'
                x, y = R - h, j
                break

    # 터지지 않았으면
    if x == -h and y == 0:
        continue

    # 클러스터 떨어트리기
    cluster1 = check(x - 1, y)
    cluster2 = check(x, y - 1)
    cluster3 = check(x, y + 1)
    cluster4 = check(x + 1, y)

    # 두개 이상이 떨어지는 경우는 없으므로 하나 이하만 값이 들어있음, 집합으로 하니까 안됨
    cluster = cluster1 + cluster2 + cluster3 + cluster4

    # 밑에꺼부터 떨어트려야함 (밑을 채우고 위를 비우는 식으로 하기때문에)
    cluster.sort(reverse=True)
    flag = False
    if cluster:
        while True:
            new_cluster = []
            dist = copy.deepcopy(cave)
            for r, c in cluster:
                if r + 1 == R or (cave[r + 1][c] == 'x' and (r + 1, c) not in cluster):
                    flag = True
                    break
                dist[r + 1][c] = 'x'
                dist[r][c] = '.'
                new_cluster.append((r + 1, c))
            if flag:
                break
            else:
                cave = dist
                cluster = new_cluster

for i in range(R):
    print(''.join(cave[i]))
