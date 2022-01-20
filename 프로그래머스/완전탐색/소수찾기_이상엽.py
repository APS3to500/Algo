from itertools import permutations

def solution(numbers):
    answer = 0
    numberList = []
    # 숫자 쪼개기
    for number in numbers:
        numberList.append(number)
        
    possible = []
    for i in range(1, len(numbers)+1):
        possible += list(permutations(numberList, i)) # 가능한 조합 넣기
    possible = list(set(possible)) # 중복 제거
    
    per_nums = []
    for poss in possible:
        per_nums.append(int(''.join(poss))) # 정수 변환 후 추가
    per_nums = list(set(per_nums)) # 중복 제거
    
    for nums in per_nums:
        if nums < 2:
            continue
        prime_num = True
        for i in range(2, int(nums**0.5)+1): # nums의 제곱근보다 작은 숫자까지만 나눠서
            if nums % i == 0:   # 하나라도 나눠지면 소수가 아니다
                prime_num = False
                break
        
        if prime_num:
            answer += 1
                
    return answer