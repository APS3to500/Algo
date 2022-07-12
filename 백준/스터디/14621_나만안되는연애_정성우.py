import sys

input = sys.stdin.readline

n, m = map(int, input().split())

genders = [0] * (n + 1)

gender = input().split()
for i in range(1, n + 1):
    if gender[i - 1] == "W":
        genders[i] = 1

parents = list(range(n + 1))
edges = []
result = 0
num = 0


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parents[b] = a
    else:
        parents[a] = b


for _ in range(m):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))

edges.sort()

for edge in edges:
    d, u, v = edge
    if find(u) != find(v) and genders[u] != genders[v]:
        union(u, v)
        result += d
        num += 1

if num == n - 1:
    print(result)
else:
    print(-1)
