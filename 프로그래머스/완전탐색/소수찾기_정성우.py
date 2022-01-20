import math
from itertools import permutations

def is_prime(n):
    if n < 2: return False

    to = int(math.sqrt(n)) + 1
    for i in range(2, to):
        if n % i == 0: return False
    return True



def solution(numbers):
    arr = list(numbers)
    l = []
    for i in range(1, len(numbers) + 1):
        temp = list(permutations(arr, i))
        for j in temp:
            l.append("".join(j))

    result = set()

    for i in l:
        result.add(int(i))

    answer = 0
    for i in result:
        if i>1:
            if is_prime(i):
                answer += 1
    return answer