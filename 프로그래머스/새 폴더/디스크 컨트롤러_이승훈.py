import heapq
def solution(jobs):
    start=list(map((lambda x:x[0] ),jobs))
    times=list(map((lambda x:x[1] ),jobs))
    heapq.heapify(times)
    print(times)
    while times:
        heapq.heappop(times)
        print(times)
    return 
solution([[0, 3], [1, 9], [2, 6]])