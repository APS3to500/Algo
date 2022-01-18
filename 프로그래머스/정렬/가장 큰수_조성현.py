def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])

    numbers = sorted(numbers, key=lambda x : x*3)

    # for i in range(len(numbers)):
    #     answer += numbers[i]

    for i in range(len(numbers)-1,-1,-1):
        answer += numbers[i]


    return str(int(answer))
        

numbers = [6, 10, 2]
print(solution(numbers))
