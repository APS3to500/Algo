# def solution(answers):
#     answer = []
#     idiot = [0]*3
#     idiot_answer = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
#     for i in range(3):
#         for j in range(len(answers)):
#             if idiot_answer[i][j%len(idiot_answer[i])] == answers[j]:
#                 idiot[i] += 1
#     smartest = max(idiot)
#     for i in range(3):
#         if idiot[i] == smartest:
#             answer.append(i+1)
#
#     return answer

def solution(numbers):
    answer = 0
    result = set()
    numbers = list(numbers)

    def permutation(k,n):
        if k == n:
            result.add(int(''.join(sel)))
            return
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = 1
                sel[k] = str(numbers[i])
                permutation(k + 1,n)
                visited[i] = 0

    for i in range(1, len(numbers) + 1):
        sel = ['0'] * i
        visited = [0] * len(numbers)
        permutation(0, i)
    print(result)
    for i in result:
        if i == 0:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            answer += 1
    return answer
answers = [1,2,3,4,5]

print(solution(answers))