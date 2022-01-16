import heapq

def solution(operations):
    heap = []
    for operation in operations:
        if operation[0] == 'I':
            heapq.heappush(heap, int(operation[2:]))
        elif operation == 'D -1' and heap:
            heapq.heappop(heap)
        elif operation == 'D 1' and heap:
            tmp = max(heap)
            idx = heap.index(tmp)
            heap.pop(idx)
    if heap:
        return [max(heap), min(heap)]
    else:
        return [0, 0]