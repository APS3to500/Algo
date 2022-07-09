row, col, k = map(int, input().split())
row -= 1
col -= 1
a = [list(map(int, input().split())) for _ in range(3)]
cnt = 0


def compile_r():
    new_a = []
    m = 0
    for r in range(len(a)):
        freq = dict()
        for c in range(len(a[0])):
            if a[r][c] == 0:
                continue
            if freq.get(a[r][c]):
                freq[a[r][c]] += 1
            else:
                freq[a[r][c]] = 1

        temp = set(a[r])
        if 0 in temp:
            temp.remove(0)

        temp = list(temp)
        temp.sort(key=lambda x: (freq[x], x))

        arr = []
        for i in temp:
            arr.append(i)
            arr.append(freq[i])

        new_a.append(arr)
        m = max(m, len(arr))

    for r in range(len(new_a)):
        for _ in range(m - len(new_a[r])):
            new_a[r].append(0)
        if len(new_a[r]) > 100:
            new_a[r] = new_a[r][:100]

    return new_a


def compile_c():
    new_a = []
    m = 0
    for c in range(len(a[0])):
        freq = dict()
        for r in range(len(a)):
            if a[r][c] == 0:
                continue

            if freq.get(a[r][c]):
                freq[a[r][c]] += 1
            else:
                freq[a[r][c]] = 1

        temp = set(list(a[r][c] for r in range(len(a))))
        if 0 in temp:
            temp.remove(0)

        temp = list(temp)
        temp.sort(key=lambda x: (freq[x], x))

        arr = []
        for i in temp:
            arr.append(i)
            arr.append(freq[i])

        new_a.append(arr)
        m = max(m, len(arr))

    for r in range(len(new_a)):
        for _ in range(m - len(new_a[r])):
            new_a[r].append(0)
        if len(new_a[r]) > 100:
            new_a[r] = new_a[r][:100]
        new_a[r] = new_a[r][::-1]

    new_a_t = [[0] * len(new_a) for _ in range(len(new_a[0]))]

    for r in range(len(new_a)):
        for c in range(len(new_a[0])):
            new_a_t[len(new_a[0]) - c - 1][r] = new_a[r][c]

    return new_a_t


while True:
    if row <= len(a) - 1 and col <= len(a[0]) - 1 and a[row][col] == k:
        break

    cnt += 1
    if cnt > 100:
        cnt = -1
        break

    if len(a) >= len(a[0]):
        a = compile_r()
    else:
        a = compile_c()

print(cnt)
