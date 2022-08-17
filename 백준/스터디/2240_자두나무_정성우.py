t, w = map(int, input().split())
jadu = [0] + [int(input()) for _ in range(t)]
dp = [[0] * (w + 1) for _ in range(t + 1)]


for i in range(1, t + 1):
    if jadu[i] == 1:
        dp[i][0] = dp[i-1][0]+1

    for j in range(1, w + 1):
        if j > i:  # 자두가 떨어진수보다 자리를 바꾸는 수가 더 클수 없으므로
            break

        if j % 2:  # 홀수라면 2에 있다
            if jadu[i] == 2:  # 먹는다
                dp[i][j] = max(dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1)
            else:  # 먹지 않는다
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])
        else:  # 짝수라면 1에 있다
            if jadu[i] == 1:  # 먹는다
                dp[i][j] = max(dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1)
            else:  # 먹지 않는다
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])

print(max(dp[t]))
