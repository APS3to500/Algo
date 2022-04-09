a = ' ' + input()
b = ' ' + input()

dp = [[0] * len(a) for _ in range(len(b))]

answer = 0
for i in range(len(b)):
    for j in range(len(a)):
        if i != 0 and j != 0:
            if a[j] == b[i]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                answer = max(answer, dp[i][j])

print(answer)
