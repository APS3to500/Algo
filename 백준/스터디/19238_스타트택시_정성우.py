import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]
n, m, fuel = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
customers = [[0] * n for _ in range(n)]
goals = [0]

start_r, start_c = map(int, input().split())

for i in range(1, m + 1):
    r1, c1, r2, c2 = map(int, input().split())
    customers[r1 - 1][c1 - 1] = i
    goals.append((r2 - 1, c2 - 1))


def drive(z, w, u, v):
    global fuel, m
    q2 = deque([(z, w)])
    temp2 = [[0] * n for _ in range(n)]
    # 출발지와 목적지가 같을때
    # if z == u and w == v:
    #     customers[z][w] = 0
    #     m -= 1
    #     return 0
    while q2:
        r2, c2 = q2.popleft()
        # 연료가 다 떨어지면
        if temp2[r2][c2] >= fuel:
            return -1
        for j in range(4):
            nr2 = r2 + dr[j]
            nc2 = c2 + dc[j]
            if 0 <= nr2 < n and 0 <= nc2 < n and temp2[nr2][nc2] == 0 and graph[nr2][nc2] == 0:
                # 목적지까지 도착하면
                if nr2 == u and nc2 == v:
                    fuel -= (temp2[r2][c2] + 1)
                    customers[z][w] = 0
                    m -= 1
                    return temp2[r2][c2] + 1
                else:
                    temp2[nr2][nc2] = temp2[r2][c2] + 1
                    q2.append((nr2, nc2))
    # 벽에 막혀서 도착을 못하게되면
    return -1


def find(x, y):
    global fuel, m
    q = deque([(x, y)])
    temp = [[0] * n for _ in range(n)]
    wait = []
    while q:
        r, c = q.popleft()

        # 지금 확인하는 곳(r,c)까지의 거리가 기존에 찾은 고객에 도달하는 거리 이상이면
        if wait and temp[wait[0][0]][wait[0][1]] <= temp[r][c] + 1:
            wait.sort(key=lambda f: (temp[f[0]][f[1]],f[0], f[1]))
            nr, nc = wait[0]
            fuel -= temp[nr][nc]
            idx = customers[nr][nc]
            res = drive(nr, nc, goals[idx][0], goals[idx][1])
            # 목적지에 도착할 수 없으면
            if res == -1:
                fuel = -1
                return
            charge = res
            fuel += (charge * 2)
            # print('after drive',fuel)
            if m == 0:
                return
            temp = [[0] * n for _ in range(n)]
            q = deque([(goals[idx][0], goals[idx][1])])
            wait = []
            continue

        # 연료가 없으면
        if temp[r][c] >= fuel:
            fuel = -1
            return

        # 출발하는 자리에 승객이 있으면
        if customers[r][c]:
            idx = customers[r][c]
            res = drive(r, c, goals[idx][0], goals[idx][1])
            if res == -1:
                fuel = -1
                return
            charge = res
            fuel += (charge * 2)
            if m == 0:
                return
            temp = [[0] * n for _ in range(n)]
            q = deque([(goals[idx][0], goals[idx][1])])
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and temp[nr][nc] == 0 and graph[nr][nc] == 0:
                if customers[nr][nc] == 0:
                    temp[nr][nc] = temp[r][c] + 1
                    q.append((nr, nc))
                else:
                    wait.append((nr, nc))
                    temp[nr][nc] = temp[r][c] + 1

    # 벽에 막혀서 더이상 갈 곳이 없으면
    fuel = -1
    return


find(start_r - 1, start_c - 1)
print(fuel)
