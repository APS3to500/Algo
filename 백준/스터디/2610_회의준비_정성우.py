import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

inf = int(1e9)


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if graph_max[a] > graph_max[b]:
        parent[a] = b
    elif graph_max[a] < graph_max[b]:
        parent[b] = a
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b


graph = [[inf] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    graph[a][a] = 0

know = []
for _ in range(m):
    a, b = map(int, input().split())
    know.append((a, b))
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

parent = [i for i in range(n + 1)]

graph_max = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] != inf:
            if graph_max[i] < graph[i][j]:
                graph_max[i] = graph[i][j]

for x, y in know:
    union(x, y)

ans = set()
for i in parent[1:]:
    ans.add(find(i))


ans = sorted(list(ans))
print(len(ans))
for i in ans:
    print(i)
