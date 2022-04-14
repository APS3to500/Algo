from collections import deque

n = int(input())

indegree = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]

take = [0] * (n + 1)
inv_graph = [[] for _ in range(n + 1)]

for a in range(1, n + 1):
    arr = list(map(int, input().split()))[:-1]
    take[a] = arr[0]
    inv_graph[a] = arr[1:]
    for b in arr[1:]:
        graph[b].append(a)
        indegree[a] += 1
result = []
q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(take[now])
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            # 건물을 동시에 지을 수 있으므로 이 노드를 더하기까지의 최대시간만 더해주면 된다
            take[i] += max(take[j] for j in inv_graph[i])
            q.append(i)

for r in take[1:]:
    print(r)
