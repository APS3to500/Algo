from collections import deque

n, k = map(int, input().split())

conveyor = deque(list(map(int, input().split())))

robot = deque([0] * n)

phase = 0
while True:
    phase += 1
    # 1
    conveyor.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    # 2
    for i in range(n - 1, 0, -1):
        if conveyor[i] > 0 and not robot[i] and robot[i - 1]:
            robot[i] = 1
            robot[i - 1] = 0
            conveyor[i] -= 1

    robot[-1] = 0

    # 3
    if not robot[0] and conveyor[0]:
        robot[0] = 1
        conveyor[0] -= 1

    # 4
    if conveyor.count(0) >= k:
        break

print(phase)
