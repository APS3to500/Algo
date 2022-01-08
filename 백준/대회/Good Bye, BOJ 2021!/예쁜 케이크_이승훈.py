import sys
def solution(num):
    if num%3==2:
        return 'TAK'
    if not num%9:
        return 'TAK'
    return 'NIE'

for m in range(int(sys.stdin.readline())):
    print(solution(int(sys.stdin.readline())))
