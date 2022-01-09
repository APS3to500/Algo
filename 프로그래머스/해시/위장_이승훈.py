def solution(clothes):
    # 분류하기 
    dresscode={}
    for i in clothes:
        if i[1] in dresscode:
            dresscode[i[1]]+=1
        else:
            dresscode[i[1]]=1
    # 가짓수만 가져오기
    arr=list(dresscode.values())

    global answer 
    answer = 1
    for j in range(len(arr)):
        answer*=(arr[j]+1)
    
    return answer-1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"],["crowmask", "face"], ["bluesunglasses", "face"]]))
