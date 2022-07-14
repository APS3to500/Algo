import sys

input = sys.stdin.readline
n, d, k, c = map(int, input().split())

sushi = [int(input()) for _ in range(n)]

# index 회전을 위해 2개를 붙임
sushi.extend(sushi)
l = 0
r = k

# 방문배열
vis = [0] * 3001

vis[c] = 1
m = 1

# 초기화
for i in range(k):
    if not vis[sushi[i]]:
        m += 1

    vis[sushi[i]] += 1

now = m

while l <= n:

    vis[sushi[l]] -= 1
    if not vis[sushi[l]]:
        now -= 1

    if not vis[sushi[r]]:
        now += 1
    vis[sushi[r]] += 1

    m = max(now, m)
    l += 1
    r += 1

print(m)
