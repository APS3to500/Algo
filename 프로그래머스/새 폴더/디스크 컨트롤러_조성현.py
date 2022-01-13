import heapq

# def solution(jobs):
#     jobs = sorted(jobs, key=lambda x: x[1])
#     answer = 0
#     start = 0
#     heap = []
#     for i in jobs:
#         heapq.heappush(heap,(i[1],i[0]))
#     print(heap)
#     while heap:
#         for i in range(len(heap)):
#             if start >= heap[i][1]:
#                 tmp = heapq.heappop(heap[i:])
#                 answer += start + tmp[0] - tmp[1]
#                 start += tmp[0]
#                 break
#             start += 1
#     answer //= len(jobs)
#     return answer

def solution(jobs):
    jobs = sorted(jobs, key=lambda x: x[1])
    answer = 0
    start = 0
    length =len(jobs)
    while jobs:
        for i in range(len(jobs)):
            if start >= jobs[i][0]:
                tmp = jobs.pop(i)
                answer += start + tmp[1] - tmp[0]
                start += tmp[1]
                break
            if i == len(jobs)-1:
                start += 1
    return answer // length

jobs = [[0, 3], [1, 9], [2, 6]]

print(solution(jobs))