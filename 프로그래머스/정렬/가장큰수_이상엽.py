# from itertools import permutations

def solution(numbers):
    # answer = '0'
    # permus = list(permutations(numbers))
    # maxi = 0
    # for number in numbers:
    #     if int(str(number)[0]) > maxi:
    #         maxi = int(str(number)[0])
    # for i in permus:
    #     tmp = ''
    #     if int(str(i[0])[0]) == maxi:
    #         for j in i:
    #             tmp += str(j)
    #         if int(tmp) > int(answer):
    #             answer = tmp
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = int(''.join(numbers))
    return str(answer)