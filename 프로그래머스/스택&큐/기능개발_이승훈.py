def solution(progresses, speeds):
#   배포 d-day 리스트
    days=[]
    for p,s in zip(progresses,speeds):
        d = (100-p)//s
        if (100-p)%s:
            d +=1
        days.append(d)

    answer = []
    idx = 0
    md = days[0]
    cnt = 0
    while idx != len(days):
        if days[idx] > md:
            md = days[idx]
            answer.append(cnt)
            cnt = 1
        else:
            cnt+=1
        idx+=1
    answer.append(cnt)
    return answer