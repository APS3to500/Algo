from copy import deepcopy

dist = [[0] * 4 for _ in range(4)]
drc = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
for i in range(4):
    arr = list(map(int, input().split()))
    for j in range(0, 8, 2):
        dist[i][j // 2] = [arr[j], arr[j + 1] - 1]
ans = 0
ans += dist[0][0][0]
dist[0][0] = [-1, dist[0][0][1]]


def shark_move(r, c, board, now):
    global ans
    ans = max(ans, now)
    board = fish_move(board)
    for k in range(1, 4):
        nr = r + drc[board[r][c][1]][0] * k
        nc = c + drc[board[r][c][1]][1] * k
        if 0 <= nr < 4 and 0 <= nc < 4 and board[nr][nc]:
            temp = deepcopy(board)
            eat = temp[nr][nc][0]
            temp[nr][nc] = [-1, temp[nr][nc][1]]
            temp[r][c] = 0
            shark_move(nr, nc, temp, now + eat)


def fish_move(board):
    for f in range(1, 17):
        flag = False
        r, c = -1, -1
        for i in range(4):
            for j in range(4):
                if board[i][j] and board[i][j][0] == f:
                    r, c = i, j
                    flag = True
                    break
            if flag:
                break
        if not flag:
            continue
        cnt = 0
        while True:
            nr = r + drc[board[r][c][1]][0]
            nc = c + drc[board[r][c][1]][1]
            if cnt == 8:
                break
            if 0 <= nr < 4 and 0 <= nc < 4 and (board[nr][nc]==0 or board[nr][nc][0] != -1):
                board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
                break
            else:
                cnt += 1
                board[r][c][1] = (board[r][c][1] + 1) % 8

    return board


shark_move(0, 0, dist, ans)
print(ans)
