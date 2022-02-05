def solution(m, n, puddles):
    d = [[0] * m for _ in range(n)]

    for puddle in puddles:
        d[puddle[1] - 1][puddle[0] - 1] = "x"

    for i in range(m):
        if d[0][i] == "x":
            for j in range(i, m):
                d[0][i] = "x"
            break
        else:
            d[0][i] = 1

    for i in range(n):
        if d[i][0] == "x":
            for j in range(i, m):
                d[j][0] = "x"
            break
        else:
            d[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            if d[i][j] == 0:
                if d[i - 1][j] == "x" and d[i][j - 1] != "x":
                    d[i][j] = d[i][j - 1]
                elif d[i][j - 1] == "x" and d[i - 1][j] != "x":
                    d[i][j] = d[i - 1][j]
                elif d[i - 1][j] == "x" and d[i][j - 1] == "x":
                    d[i][j] = "x"
                else:
                    d[i][j] = d[i - 1][j] + d[i][j - 1]
    return d[-1][-1] % 1000000007
