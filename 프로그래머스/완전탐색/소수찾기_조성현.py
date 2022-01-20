def permutation(idx):
    global result
    if idx == len(numbers):
        print(sel)
        result.add(int("".join(sel)))
        return
    for i in range(len(numbers)):
        if check[i] == 0:
            sel[idx] = numbers[i]
            check[i] = 1
            permutation(idx+1)
            check[i] = 0

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    permutation(0)
    for i in result:
        if i == 0:
            continue
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            answer += 1
    return answer

numbers = "17"
result = set()
check = [0] * len(numbers)
sel = [0] * len(numbers)
print(solution(numbers))
