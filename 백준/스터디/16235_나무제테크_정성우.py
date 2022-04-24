import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
d = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
A = [list(map(int, input().split())) for _ in range(n)]
tree = [[list() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

land = [[5] * n for _ in range(n)]

for _ in range(k):
    # spring
    for r in range(n):
        for c in range(n):
            if tree[r][c]:
                tree[r][c].sort()
                for i in range(len(tree[r][c])):
                    if tree[r][c][i] <= land[r][c]:
                        land[r][c] -= tree[r][c][i]
                        tree[r][c][i] += 1
                    else:
                        # summer
                        for j in range(i, len(tree[r][c])):
                            land[r][c] += tree[r][c][j] // 2
                        tree[r][c] = tree[r][c][:i]
                        break

    # fall
    for r in range(n):
        for c in range(n):
            for i in range(len(tree[r][c])):
                if tree[r][c][i] % 5 == 0:
                    for dr, dc in d:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            tree[nr][nc].append(1)
    # winter
    for r in range(n):
        for c in range(n):
            land[r][c] += A[r][c]

ans = 0

for r in range(n):
    for c in range(n):
        ans += len(tree[r][c])
print(ans)
