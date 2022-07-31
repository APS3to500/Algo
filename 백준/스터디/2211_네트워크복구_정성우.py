import heapq
import sys

input = sys.stdin.readline

inf = int(1e9)

n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]

distance = [inf] * (n + 1)
line = [0] * (n + 1)
start = 1

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

ans = 0


def dijkstra(start):
    global ans
    q = []

    heapq.heappush(q, (0, start))

    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                if not line[i[0]]:
                    ans += 1
                line[i[0]] = (now, i[0])


dijkstra(start)

print(ans)
for i in line:
    if i:
        print(i[0], i[1])
