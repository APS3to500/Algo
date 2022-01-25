def solution(n, lost, reserve):
    l = set(lost) - set(reserve)
    r = set(reserve) - set(lost)

    for i in r:
        if i - 1 in l:
            l.remove(i - 1)
        elif i + 1 in l:
            l.remove(i + 1)

    return n - len(l)
