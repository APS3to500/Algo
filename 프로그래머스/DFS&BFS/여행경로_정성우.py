tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]


def dfs(start):
    global path, visited, t, answer

    if all(visited) and len(t) == len(path) - 1:
        answer = path[:]
        return

    for j in range(len(t)):
        if not visited[j] and t[j][0] == start:
            visited[j] = True
            path.append(t[j][1])
            dfs(t[j][1])
            if all(visited):
                return
            visited[j] = False
            path.pop()


def solution(tickets):
    global path, visited, t, answer
    answer = []
    t = tickets
    t.sort(key=lambda x: x[1])
    visited = [False] * len(t)
    path = ["ICN"]
    for i in range(len(t)):
        if t[i][0] == "ICN":
            visited[i] = True
            path.append(t[i][1])
            dfs(t[i][1])
            path.pop()
            visited[i] = False
    return answer


print(solution(tickets))
