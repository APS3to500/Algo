import sys
from collections import deque

input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def bfs():
    q = deque()
    q.append((0, 0, 0, 1))
    while q:
        r, c, broken, cnt = q.popleft()
        if r == n - 1 and c == m - 1:
            print(cnt)
            return

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc][broken]:
                visited[nr][nc][broken] = 1

                if not graph[nr][nc]:
                    q.append((nr, nc, broken, cnt + 1))

                elif graph[nr][nc] and broken < k:
                    q.append((nr, nc, broken + 1, cnt + 1))
    print(-1)


n, m, k = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]

bfs()
