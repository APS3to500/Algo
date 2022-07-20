n=int(input())

arr = list(map(int,input().split()))

k = int(input())

dp = [[0]*(n+1) for _ in range(3)]

s = [0]

for a in arr:
    s.append(s[-1]+a)


for i in range(3):
    for j in range(i*k+1,n+1):
        dp[i][j]= max(dp[i][j-1], dp[i-1][j-k]+s[j]-s[j-k])

print(dp[2][n])