n, m, k = map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
sharks = [[0] * n for _ in range(n)]
smell = [[0] * n for _ in range(n)]
prior = dict()
dir = dict()
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j]:
            # [상어 번호, 냄새 지속 시간]
            smell[i][j] = [arr[j], k]
            sharks[i][j] = arr[j]

arr = list(map(int, input().split()))
for i in range(m):
    dir[i + 1] = arr[i] - 1

for i in range(1, m + 1):
    prior[i] = []
    for _ in range(4):
        prior[i].append(list(map(lambda x: int(x) - 1, input().split())))

time = 0
while True:
    time += 1

    temp = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if sharks[r][c]:
                num = sharks[r][c]
                flag = False
                # 아무 냄새가 없는 칸 찾기
                for d in prior[num][dir[num]]:
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < n and 0 <= nc < n:
                        if not smell[nr][nc]:
                            flag = True
                            dir[num] = d
                            if temp[nr][nc]:
                                m -= 1
                                if temp[nr][nc] > num:
                                    temp[nr][nc] = num
                            else:
                                temp[nr][nc] = num
                            break

                # 자기 냄새가 있는 칸 찾기
                if not flag:
                    for d in prior[num][dir[num]]:
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if 0 <= nr < n and 0 <= nc < n:
                            if smell[nr][nc] and smell[nr][nc][0] == num:
                                dir[num] = d
                                temp[nr][nc] = num
                                break
    sharks = temp
    # 냄새 처리(추가 or 제거 or 줄이기)
    for r in range(n):
        for c in range(n):
            if smell[r][c] and not sharks[r][c]:
                smell[r][c][1] -= 1
                if smell[r][c][1] == 0:
                    smell[r][c] = 0
            if sharks[r][c]:
                smell[r][c] = [sharks[r][c], k]
    if m == 1:
        break

    if time == 1000 and m > 1:
        time = -1
        break
print(time)
