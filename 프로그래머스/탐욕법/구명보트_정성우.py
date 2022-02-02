def solution(people, limit):
    answer = len(people)
    people.sort()
    l = 0
    r = len(people) - 1
    while l < r:
        if people[l] + people[r] > limit:
            r -= 1
        else:
            l += 1
            r -= 1
            answer -= 1
    return answer
