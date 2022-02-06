from collections import deque


def bfs(x, y, computers, n):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if computers[x][y] == 1:
            computers[x][y] = 0
            computers[y][x] = 0
            for z in range(n):
                q.append((y, z))


def solution(n, computers):
    answer = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                bfs(i, j, computers, n)
                answer += 1
    return answer
