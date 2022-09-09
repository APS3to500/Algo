n, m = map(int, input().split())
k = int(input())

dp = [[0] * (m + 1) for _ in range(n + 1)]

hole = set()
dp[1][1] = 1
for _ in range(k):
    x, y = map(int, input().split())
    hole.add((x, y))

for j in range(1, m + 1):
    for i in range(1, n + 1):
        if (i, j) in hole:
            continue
        # 위에서 옴
        dp[i][j] += dp[i - 1][j]

        # 왼쪽 대각 아래에서 옴
        if j % 2:
            dp[i][j] += dp[i][j - 1]
        elif not j % 2 and i < n:
            dp[i][j] += dp[i + 1][j - 1]

        # 왼쪽 대각 위에서 옴
        if j % 2:
            dp[i][j] += dp[i - 1][j - 1]
        else:
            dp[i][j] += dp[i][j - 1]

print(dp[n][m] % (1000000007))
