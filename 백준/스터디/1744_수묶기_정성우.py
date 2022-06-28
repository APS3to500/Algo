import sys

input = sys.stdin.readline

n = int(input())
minus = []
plus = []
one = []
zero = False
for _ in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num < 0:
        minus.append(num)
    elif num == 1:
        one.append(num)
    else:
        zero = True

plus.sort(reverse=True)
minus.sort()
ans = 0

if len(plus) % 2:
    for i in range(0, len(plus) - 1, 2):
        ans += plus[i] * plus[i + 1]
    ans += plus[-1]
else:
    for i in range(0, len(plus), 2):
        ans += plus[i] * plus[i + 1]

if len(minus) % 2:
    for i in range(0, len(minus) - 1, 2):
        ans += minus[i] * minus[i + 1]
    if not zero:
        ans += minus[-1]
else:
    for i in range(0, len(minus), 2):
        ans += minus[i] * minus[i + 1]

print(ans + len(one))
