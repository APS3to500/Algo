def solution(alp, cop, problems):
    inf = int(1e9)
    l = len(problems)
    alp_max = max([problems[i][0] for i in range(l)])
    cop_max = max([problems[i][1] for i in range(l)])

    dp = [[inf] * (alp_max + 200) for _ in range(cop_max + 200)]

    if alp_max <= alp and cop_max <= cop:
        return 0

    if alp >= alp_max:
        alp = alp_max

    if cop >= cop_max:
        cop = cop_max

    dp[alp][cop] = 0

    for i in range(alp, alp_max + 1):
        for j in range(cop, cop_max + 1):
            dp[i][j + 1] = min(dp[i][j] + 1, dp[i][j + 1])
            dp[i + 1][j] = min(dp[i][j] + 1, dp[i + 1][j])

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:

                    if i + alp_rwd > alp_max and j + cop_rwd > cop_max:
                        dp[alp_max][cop_max] = min(dp[i][j] + cost, dp[alp_max][cop_max])

                    elif i + alp_rwd <= alp_max and j + cop_rwd <= cop_max:
                        dp[i + alp_rwd][j + cop_rwd] = min(dp[i][j] + cost, dp[i + alp_rwd][j + cop_rwd])

                    elif i + alp_rwd > alp_max:
                        dp[alp_max][j + cop_rwd] = min(dp[i][j] + cost, dp[alp_max][j + cop_rwd])

                    elif j + cop_rwd > cop_max:
                        dp[i + alp_rwd][cop_max] = min(dp[i][j] + cost, dp[i + alp_rwd][cop_max])

    return dp[alp_max][cop_max]
