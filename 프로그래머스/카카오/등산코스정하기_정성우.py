import heapq

def dijkstra(gates):
    global summits_set, gates_set, intensity, graph
    q = []
    for start in gates:
        heapq.heappush(q, (0, start))
        intensity[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if intensity[now] < dist:
            continue

        for next_node, next_cost in graph[now]:
            if next_node in gates_set:
                continue

            if intensity[next_node] > max(intensity[now], next_cost):
                intensity[next_node] = max(intensity[now], next_cost)
                heapq.heappush(q, (intensity[next_node], next_node))


def solution(n, paths, gates, summits):
    global summits_set, gates_set, intensity, graph
    inf = int(1e9)
    intensity = [inf] * (n + 1)
    graph = [[] for i in range(n + 1)]
    summits_set = set(summits)
    gates_set = set(gates)

    for a, b, c in paths:
        if a not in summits_set and b not in gates_set:
            graph[a].append((b, c))
        if b not in summits_set and a not in gates_set:
            graph[b].append((a, c))

    dijkstra(gates)

    answer1 = -1
    answer2 = inf

    for i in range(len(intensity)):
        if i in summits_set and intensity[i] and answer2 > intensity[i]:
            answer1 = i
            answer2 = intensity[i]

    return answer1, answer2