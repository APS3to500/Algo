import heapq
import sys

input = sys.stdin.readline

inf = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [inf] * (n + 1)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, next_cost in graph[now]:
            cost = dist + next_cost
            if distance[next_node] > cost:
                distance[next_node] = cost

                heapq.heappush(q, (cost, next_node))
    return distance


for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    candidate = [int(input()) for _ in range(t)]
    ans = []
    from_s = dijkstra(s)
    from_g = dijkstra(g)
    from_h = dijkstra(h)

    for c in candidate:
        if from_s[g] + from_g[h] + from_h[c] == from_s[c] or from_s[h] + from_h[g] + from_g[c] == from_s[c]:
            ans.append(c)
    ans.sort()
    print(*ans)
