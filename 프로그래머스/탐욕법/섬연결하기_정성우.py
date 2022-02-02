def find(x, parents):
    if parents[x] != x:
        parents[x] = find(parents[x], parents)
    return parents[x]


def union(x, y, parents):
    a = find(x, parents)
    b = find(y, parents)
    if a <= b:
        parents[b] = a
    else:
        parents[a] = b


def solution(n, costs):
    answer = 0
    parents = [i for i in range(n)]
    islands = []

    for cost in costs:
        a, b, c = cost
        islands.append((c, a, b))

    islands.sort()

    for island in islands:
        c, a, b = island
        if find(a, parents) != find(b, parents):
            union(a, b, parents)
            answer += c

    return answer
