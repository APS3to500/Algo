import heapq

def solution(jobs):
    answer = 0
    st = -1
    now = 0
    idx = 0
    heap = []

    while idx < len(jobs):
        for job in jobs:
            if st < job[0] <= now: # 현재 처리할 수 있는 작업이면
                heapq.heappush(heap, [job[1], job[0]])
        
        if heap:
            tmp = heapq.heappop(heap)
            st = now
            now += tmp[0]
            answer += now - tmp[1]
            idx += 1
        else:
            now += 1
    
    return answer // len(jobs)