def solution(m, n, puddles):
    answer = 0
    puddles = set(puddles)
    zido = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                zido[i][j] = 1
            elif (j, i) not in puddles:
                zido[i][j] = zido[i-1][j] + zido[i][j-1]
    
    answer = zido[n][m] % 1000000007
    return answer