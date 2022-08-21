n = [0] + list(map(int, input()))
l = len(n)
dp = [0] * (l + 1)
dp[0] = dp[1] = 1

if not n[1]:
    print(0)
else:
    for i in range(2, l):
        if n[i] > 0:
            dp[i] = dp[i - 1]

        temp = n[i - 1] * 10 + n[i]
        if 10 <= temp <= 26:
            dp[i] += dp[i - 2]

    print(dp[l - 1] % 1000000)
