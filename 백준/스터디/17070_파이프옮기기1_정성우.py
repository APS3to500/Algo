n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dist = [[[0] * n for _ in range(n)] for _ in range(3)]

# 0:가로, 1: 세로, 2: 대각선

# 첫 줄 가로는 모두 1
for i in range(n):
    if graph[0][i]:
        break
    dist[0][0][i] = 1

for i in range(1, n):
    for j in range(2, n):
        if not graph[i][j]:
            # 가로
            dist[0][i][j] = dist[0][i][j - 1] + dist[2][i][j - 1]
            # 세로
            dist[1][i][j] = dist[1][i - 1][j] + dist[2][i - 1][j]
            # 대각선
            if graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
                dist[2][i][j] = dist[0][i - 1][j - 1] + dist[1][i - 1][j - 1] + dist[2][i - 1][j - 1]

answer = 0
for k in range(3):
    answer += dist[k][n - 1][n - 1]
print(answer)
