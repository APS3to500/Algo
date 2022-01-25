# print(ord('Z')-ord('A'))
def solution(name):
    answer = 0
    s_idx = 0
    e_idx = 0
    b= 0
    for i in range(1,len(name)):
        if name[i] == 'A':
            s_idx = i
            for j in range(i+1,len(name)):
                if name[j] != 'A':
                    e_idx = j -1
            break
    a = (s_idx-1) * 2 + (len(name)-e_idx)

    for i in range(len(name)-1,-1,-1):
        if name[i] == 'A':
            for j in range(i-1,-1,-1):
                if name[j] != 'A':
                    b = len(name) -1 -j
            break
    if s_idx==0:
        answer += len(name) -1
    else:
        answer += min(a,b)

    for j in name:
        if ord(j) - ord('A') <= 13:
            answer += ord(j) - ord('A')
        else:
            answer += 26 - (ord(j) - ord('A'))

    return answer
name ="ABAAAAAAAAABB"
print(solution(name))
