def solution(number, k):
    answer = ''
    result = []
    for i in range(len(number)):
        if not result:
            result.append(number[i])
            continue
        if k > 0:
            while result[-1] < number[i]:
                result.pop()
                k -= 1
                if not result or k == 0:
                    break
        result.append(number[i])
    if k > 0:
        result = result[:-k]
    answer = ''.join(result)
    return answer

number = "4177252841"
k = 4
print(solution(number,k))
