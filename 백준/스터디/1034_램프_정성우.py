n, m = map(int, input().split())

lamp = [list(map(int, list(input()))) for _ in range(n)]
k = int(input())

ans = 0
for i in range(n):
    zero_cnt = lamp[i].count(0)
    if zero_cnt <= k and zero_cnt % 2 == k % 2:
        zero_pos = []
        for j in range(m):
            if not lamp[i][j]:
                zero_pos.append(j)
        cnt = 0
        for l in range(i, n):
            temp = []

            for j in range(m):
                if not lamp[l][j]:
                    temp.append(j)
            if temp == zero_pos:
                cnt += 1

        if cnt > ans:
            ans = cnt

print(ans)
