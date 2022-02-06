def dfs(i,computers):
    computers[i][i]=987654321 
    for j in range(len(computers[i])):
        if computers[i][j]==1:
            dfs(j,computers)
    
    
def solution(n, computers):
    answer = 0

    for i in range(n):
        if computers[i][i]==1:
            dfs(i,computers)
            answer+=1
    return answer