def solution(clothes):
    def comb(n,r):
        global answer
        if not r:
            al=1
            for s in t:
                al*=s
            answer += al
            print(al)
            return 
        elif n<r:
            return  
        else:
            t[r-1]=arr[n-1]
            comb(n-1,r-1)
            comb(n-1,r)
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
    answer = 0
    for j in range(1,len(arr)+1):
        t = [0]*j
        comb(len(arr),j)
    
    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"],["crowmask", "face"], ["bluesunglasses", "face"]]))
