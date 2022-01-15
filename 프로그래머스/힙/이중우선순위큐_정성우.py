import heapq

def solution(operations):
    minheap = []
    maxheap = []
    nums = dict()

    for operation in operations:
        cmd, data = operation.split()
        data = int(data)
        if cmd == 'I':
            heapq.heappush(minheap, data)
            heapq.heappush(maxheap, -data)

            if nums.get(data):
                nums[data] += 1
            else:
                nums[data] = 1
        else:
            if not minheap:
                continue
            if not maxheap:
                continue

            if data == 1:
                while True:
                    if not maxheap:
                        break
                    maxvalue = heapq.heappop(maxheap)

                    if nums[-maxvalue] >= 1:
                        nums[-maxvalue] -= 1
                        break
            else:
                while True:
                    if not minheap:
                        break
                    minvalue = heapq.heappop(minheap)
                    if nums[minvalue] >= 1:
                        nums[minvalue] -= 1
                        break
    flag=True
    for cnt in nums.values():
        if cnt:
            flag=False
            break


    if flag:
        return [0, 0]
    else:
        while True:
            maxvalue = heapq.heappop(maxheap)
            if nums[-maxvalue] >= 1:
                nums[-maxvalue] -= 1
                break

        while True:
            minvalue = heapq.heappop(minheap)
            if nums[minvalue] >= 1:
                nums[minvalue] -= 1
                break

        return [-maxvalue, minvalue]