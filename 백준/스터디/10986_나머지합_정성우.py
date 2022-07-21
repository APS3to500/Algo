import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

ans = 0
base = 0
group = dict()

for a in arr:
    base += a
    if group.get(base % m):
        group[base % m].append(base)
    else:
        group[base % m] = [base]

for key in group:
    l = len(group[key])
    ans += l * (l - 1) // 2
    if not key % m:
        ans += l
print(ans)
