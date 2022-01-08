import sys
def solution(num):
    ndic=[]
    n = 1
    while 1:
        n+=1
        for i in ndic:
            if not n%i:
                break
        else:
            ndic.append(n)
        if len(ndic)>1:
            ans = ndic[-1] * ndic[-2]
            if ans>num:
                break
    return ans
print(solution(int(sys.stdin.readline())))