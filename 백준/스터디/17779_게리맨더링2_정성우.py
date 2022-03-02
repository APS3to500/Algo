import sys

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

total = 0
answer = 987654321
for row in graph:
    total += sum(row)


def calc(x, y, d1, d2):
    section = [0] * 5

    c = y + 1
    for r in range(x + d1):
        if r >= x:
            c -= 1
        section[0] += sum(graph[r][:c])

    c = y + 1
    for r in range(x + d2 + 1):
        if r > x:
            c += 1
        section[1] += sum(graph[r][c:])

    c = y - d1
    for r in range(x + d1, n):
        section[2] += sum(graph[r][:c])
        if r < x + d1 + d2:
            c += 1

    c = y + d2
    for r in range(x + d2 + 1, n):
        section[3] += sum(graph[r][c:])
        if r <= x + d1 + d2:
            c -= 1

    section[4] = total - sum(section)
    return max(section) - min(section)


for x in range(n - 2):
    for y in range(1, n - 1):
        for d1 in range(1, n - 1):
            for d2 in range(1, n - 1):
                if x + d1 + d2 >= n:
                    continue
                if y - d1 < 0:
                    continue
                if y + d2 >= n:
                    continue
                answer = min(answer, calc(x, y, d1, d2))

print(answer)
