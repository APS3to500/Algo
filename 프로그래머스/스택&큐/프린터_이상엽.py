def solution(priorities, location):
    answer = 1
    while True:
        tmp = priorities[0]
        for pr in priorities:
            if pr > tmp:
                if location == 0:
                    location = len(priorities)-1
                else:
                    location -= 1
                priorities.pop(0)
                priorities.append(tmp)
                break
        else:
            if location == 0:
                return answer
            else:
                answer += 1
                location -= 1
                priorities.pop(0)