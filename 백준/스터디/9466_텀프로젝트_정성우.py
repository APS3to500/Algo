import sys

sys.setrecursionlimit(111111)
input = sys.stdin.readline


def dfs(x):
    global cnt
    next = student[x]
    visited[x] = 1
    cycle.append(x)
    if visited[next]:  # cycle 발생
        if next in cycle:
            idx = -1
            for j in range(len(cycle)):
                if cycle[j] == next:
                    idx = j
                    break
            if idx != -1:
                cnt += len(cycle[idx:])
        return

    dfs(next)


for _ in range(int(input())):
    n = int(input())
    student = [0] + list(map(int, input().split()))

    visited = [0] * (n + 1)

    cnt = 0
    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n - cnt)

# 1
# 3
# 2 3 2

# 1
