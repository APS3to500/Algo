n = int(input())
building = list(map(int, input().split()))
ans = 0

for i in range(n):
    cnt = 0
    mn = int(1e10)
    # 왼쪽
    for j in range(i - 1, -1, -1):
        if (building[i] - building[j]) / (i - j) < mn:
            mn = (building[i] - building[j]) / (i - j)
            cnt += 1

    mx = -int(1e10)
    # 오른쪽
    for j in range(i + 1, n):
        if (building[j] - building[i]) / (j - i) > mx:
            mx = (building[j] - building[i]) / (j - i)
            cnt += 1

    ans = max(cnt, ans)
print(ans)
