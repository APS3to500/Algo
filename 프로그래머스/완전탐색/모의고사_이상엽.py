def solution(answers):
    answer = []
    person1 = [1,2,3,4,5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a1 = 0
    a2 = 0
    a3 = 0
    for i in range(len(answers)):
        if person1[i%len(person1)] == answers[i]:
            a1 += 1
        if person2[i%len(person2)] == answers[i]:
            a2 += 1
        if person3[i%len(person3)] == answers[i]:
            a3 += 1
    if a1 == a2 == a3:
        answer =[1, 2, 3]
    elif a1 == a2 > a3:
        answer = [1, 2]
    elif a1 == a3 > a2:
        answer = [1, 3]
    elif a2 == a3 > a1:
        answer = [2, 3]
    elif max(a1, a2, a3) == a1:
        answer = [1]
    elif max(a1, a2, a3) == a2:
        answer = [2]
    else:
        answer = [3]
            
    return answer