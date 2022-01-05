def solution(participant, completion):
    run=dict()
    for i in participant:
        run[i]=0
    for j in participant:
        run[j]+=1
    for k in completion:
        run[k]-=1
    for l in participant:
        if run[l]==1:
            answer=l
            break
    return answer