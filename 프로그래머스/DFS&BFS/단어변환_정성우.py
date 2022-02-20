def dfs(now, cnt, v, t, w):
    global answer
    if now == t:
        answer = min(answer, cnt)
        return

    for k in range(len(w)):
        if not v[k]:
            tmp = 0
            for l in range(len(t)):
                if now[l] == w[k][l]:
                    tmp += 1
            if tmp == len(now) - 1:
                v[k] = True
                dfs(w[k], cnt + 1, v, t, w)
                v[k] = False


def solution(begin, target, words):
    global answer
    answer = 52
    visited = [False] * len(words)
    for i in range(len(words)):
        cnt = 0
        for j in range(len(target)):
            if begin[j] == words[i][j]:
                cnt += 1
        if cnt == len(begin) - 1:
            visited[i] = True
            dfs(words[i], 1, visited, target, words)
            visited[i] = False
    if answer == 52:
        answer = 0
    return answer
