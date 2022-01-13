import heapq
def solution(operations):
    answer = [0, 0]
    heap = []
    max_heap =[]
    for i in operations:
        operation = i.split()
        if operation[0] == "I":
            tmp = int(operation[1])
            heapq.heappush(heap,tmp)
            heapq.heappush(max_heap,(-tmp,tmp))
        else:
            if not heap:
                continue
            if int(operation[1]) == 1:
                max_num = heapq.heappop(max_heap)[1]
                heap.remove(max_num)
            else:
                min_num = heapq.heappop(heap)
                max_heap.remove((min_num*-1,min_num))
    if heap:
        answer = [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    return answer
operations = ["I 7","I 5","I -5","D -1"]
print(solution(operations))
