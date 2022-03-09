import sys
from itertools import permutations

input = sys.stdin.readline
answer = 0
perms = permutations(list(range(1, 9)))
n = int(input())
predict = []
for _ in range(n):
    predict.append(list(map(int, input().split())))

for perm in perms:
    order = list(perm)
    players = order[:3] + [0] + order[3:]
    idx = 0
    score = 0
    for i in range(n):
        out = 0
        base1, base2, base3 = 0, 0, 0

        while out < 3:
            hit = predict[i][players[idx]]
            if not hit:
                out += 1

            elif hit == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2

            elif hit == 2:
                score += base3 + base2
                base1, base2, base3 = 0, 1, base1
            elif hit == 3:
                score += base3 + base2 + base1
                base1, base2, base3 = 0, 0, 1
            else:
                score += base3 + base2 + base1 + 1
                base1, base2, base3 = 0, 0, 0
            idx += 1
            idx %= 9

    answer = max(answer, score)
print(answer)
