import sys

input = sys.stdin.readline

n = int(input())

u = []
for _ in range(n):
    u.append(int(input()))

arr1 = set()  # x+y
for x in range(n):
    for y in range(n):
        arr1.add(u[x] + u[y])

cand = []  # k
for k in range(n-1, -1, -1):
    for z in range(n):
        if u[k] - u[z] in arr1:
            cand.append(u[k])
cand.sort()
print(cand[-1])
