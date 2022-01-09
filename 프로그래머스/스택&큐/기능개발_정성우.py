from collections import deque

def solution(progresses, speeds):
    answer = []
    
    proq=deque(progresses)
    spdq=deque(speeds)
    day=0
    
    while proq:
        
        cnt=0
        while proq[0]<100:
            day+=1
            proq[0]+=spdq[0]
            
        #100이상이면
        cnt+=1
        proq.popleft()
        spdq.popleft()
        
        while proq:
            
            proq[0]+=spdq[0]*day
            
            if proq[0]>=100:
                proq.popleft()
                spdq.popleft()
                cnt+=1
            else:
                break
                
        answer.append(cnt)
         
    return answer


def solution2(progresses, speeds):
    answer = []
    prgq=deque(progresses)
    spdq=deque(speeds)
    day=1
    while prgq:
        progress=prgq.popleft()
        speed=spdq.popleft()
        progress+=speed*day
        if progress>=100:
            answer[-1]+=1
        else:
            answer.append(1)
            while progress<100:
                progress+=speed
                day+=1
            
        
    return answer