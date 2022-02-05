def solution(triangle):
    d = [[0] * n for n in range(1, len(triangle) + 1)]
    d[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                d[i][0] = d[i - 1][0] + triangle[i][0]
            elif j == (len(triangle[i]) - 1):
                d[i][-1] = d[i - 1][-1] + triangle[i][-1]
            else:
                d[i][j] = max(d[i - 1][j - 1] + triangle[i][j], d[i - 1][j] + triangle[i][j])
    return max(d[len(triangle) - 1])
