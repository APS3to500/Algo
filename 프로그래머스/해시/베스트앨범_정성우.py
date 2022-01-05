def solution(genres, plays):
    answer = []
    d={}
    for g in genres:
        d[g]=0
    for i,j in zip(genres,plays):
        d[i]+=j
    new_list=sorted(d.items(),key= lambda x:x[1], reverse=True)
    answer={}
    rank=0
    for a,b in new_list:
        temp=[]
        for i,j in enumerate(zip(genres,plays)):
            if j[0]==a:
                temp.append((i,j[1]))
        temp.sort(key=lambda x : x[1],reverse=True)
        cnt=0
        for i in temp:
            answer[i[0]]=rank
            rank+=1
            cnt+=1
            if cnt==2:
                break
    
    return list(answer.keys())