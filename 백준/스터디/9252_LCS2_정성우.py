a = [0] + list(input())
b = [0] + list(input())

m = len(a)
n = len(b)

dp = [[""] * n for _ in range(m)]

for i in range(1, m):
    for j in range(1, n):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + a[i]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print(len(dp[m - 1][n - 1]))
print(dp[m - 1][n - 1])
