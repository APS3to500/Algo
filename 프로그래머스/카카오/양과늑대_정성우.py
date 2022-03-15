vis = [False] * 17
left = [-1] * 17
right = [-1] * 17


def move(sheep, wolf, now):
    global answer
    if node[now]:
        wolf += 1
    else:
        sheep += 1

    if sheep <= wolf:
        return

    if sheep > answer:
        answer = sheep

    for i in range(n):
        if vis[i]:
            for branch in (left[i], right[i]):
                if branch == -1:
                    continue
                if not vis[branch]:
                    vis[branch] = True
                    move(sheep, wolf, branch)
                    vis[branch] = False


def solution(info, edges):
    global n, node, answer
    node = info[:]

    n = len(info)
    for p, c in edges:
        if left[p] != -1:
            right[p] = c
        else:
            left[p] = c
    answer = 0
    vis[0] = True
    move(0, 0, 0)

    return answer