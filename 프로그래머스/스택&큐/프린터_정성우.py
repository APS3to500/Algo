
from collections import deque

def solution(priorities, location):
    answer = 0
    q=deque()
    
    for i, v in enumerate(priorities):
        q.append((i,v))
        
    while q:
        max_prior=0
        # 최대 중요도 찾기
        for i in range(len(q)):
            if q[i][1]>max_prior:
                max_prior=q[i][1]
                
        while True:
            idx,priority=q.popleft()
            # 최대 중요도이면 꺼내기
            if priority==max_prior:
                # 찾고자 하는 위치면 리턴
                if idx==location:
                    return answer+1
                # 아니면 꺼낸 횟수+1
                else:
                    answer+=1
                    break
            # 아니면 다시 넣기
            else:
                q.append((idx,priority))


def solution2(priorities, location):
    answer = 0
    prq = deque([])
    now = 0
    for i, v in enumerate(priorities):
        prq.append((i, v))
        
    while prq:
        maxv=max(prq, key= lambda x : x[1])[1]
        i, v = prq.popleft()
        if v == maxv:
            now += 1
            if i == location:
                answer = now
                break
        else:
            prq.append((i, v))

    return answer