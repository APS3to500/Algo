def solution(priorities, location):
    answer = 1
    while True:
        for i in range(len(priorities)):
            if priorities[i] > priorities[0]:
                tmp = priorities.pop(0)
                priorities.append(tmp)
                if location == 0:
                    location = len(priorities)-1
                else:
                    location -= 1
                break
        else:
            if location == 0:
                return answer
            else:
                answer += 1
                location -= 1
                tmp = priorities.pop(0)
                priorities.append(0)


    return answer

priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities,location))