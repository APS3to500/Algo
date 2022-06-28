n, k = map(int, input().split())

order = list(map(int, input().split()))

multitab = [0] * n

ans = 0

for i in range(k):
    if order[i] in multitab:
        continue
    else:
        isFinished = False
        for j in range(len(multitab)):
            if multitab[j] == 0:
                multitab[j] = order[i]
                isFinished = True
                break

        if isFinished:
            continue

        ans += 1
        idx = -1
        hole = 0
        for j in range(len(multitab)):
            if multitab[j] in order[i:]:
                temp = order[i:].index(multitab[j])
                if temp > idx:
                    idx = temp
                    hole = j
            else:
                multitab[j] = order[i]
                isFinished = True
                break

        if isFinished:
            continue

        multitab[hole] = order[i]

print(ans)
