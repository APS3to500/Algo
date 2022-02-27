import heapq


def dijkstra(distance, graph):
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))


def solution(n, vertex):
    INF = int(1e9)
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for i in vertex:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    dijkstra(distance, graph)
    distance[0] = 0
    return distance.count(max(distance))