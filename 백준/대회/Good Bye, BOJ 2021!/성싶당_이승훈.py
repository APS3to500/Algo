import sys

N, G, K = map(int,sys.stdin.readline().split())
ops = []
nes = []
for n in range(N):
    S, L, O = map(int,sys.stdin.readline().split())
    if O:
        ops.append([S, L])
    else:
        nes.append([S, L])
x = 1
while 1:
    x += 1
    # 필수
    ng = 0
    for i in nes:
        ng+=i[0]*max(1,x-i[1])
    # 옵션
    og=[]
    for j in ops:
        og.append(j[0]*max(1,x-j[1]))
    og.sort()
    # 세균
    ng+=sum(og[:len(og)-K])
    if ng>G:
        break
print(x-1)