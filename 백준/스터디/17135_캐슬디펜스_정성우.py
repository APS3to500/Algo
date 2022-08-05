from itertools import combinations
from collections import deque
import copy

dr = [0, -1, 1, 0]
dc = [-1, 0, 0, 1]


def bfs(archer):
    global score
    q = deque()
    q.append((n, archer, 0))
    visited = [[0] * m for _ in range(n)]
    while q:
        r, c, distance = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and distance < d:
                if dist[nr][nc] == 1:
                    enemies.add((nr, nc))
                    return
                else:
                    q.append((nr, nc, distance + 1))
                    visited[nr][nc] = 1


n, m, d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

comb = combinations(range(m), 3)

ans = 0
for f, s, t in comb:
    dist = copy.deepcopy(graph)
    # 궁수 배치
    temp = [0] * m
    temp[f], temp[s], temp[t] = 1, 1, 1
    dist.append(temp)

    score = 0
    for _ in range(n):
        # 동시로 공격받는 적처리를 위함
        enemies = set()
        # 궁수가 쏠 적들 찾기
        bfs(f)
        bfs(s)
        bfs(t)

        # 화살 쏘기
        for r, c in enemies:
            dist[r][c] = 0
            score += 1

        # 적이 아래로 이동
        for i in range(m):
            for j in range(n - 1, 0, -1):
                dist[j][i] = dist[j - 1][i]
            dist[0][i] = 0

    ans = max(score, ans)

print(ans)
