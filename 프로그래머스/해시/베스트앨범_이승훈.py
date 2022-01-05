def solution(genres, plays):
    gdic = {}
    ndic = {}
    for i in enumerate(genres):
        idx=i[0]
        g=i[1]
        if g in gdic:
            gdic[g].append([plays[idx],idx])
            gdic[g].sort(reverse=True)
            if len(gdic[g])>2:
                gdic[g].pop()
            ndic[g]+=plays[idx]
        else:
            gdic[g]=[[plays[idx],idx]]
            ndic[g]=plays[idx]
    ndic = sorted(ndic.items(), key=lambda x: x[1], reverse=True)
    answer=[]
    for k,v in ndic:
        if len(gdic[k])>1:
            a = gdic[k][0]
            b = gdic[k][1]
            if a[0]==b[0]:
                if a[1]>b[1]:
                    a,b = b,a
            answer.append(a[1])
            answer.append(b[1])
        else:
            answer.append(gdic[k][0][1])
    return answer

g=["classic", "pop", "classic", "classic", "pop"]
p=[500, 600, 800, 800, 2500]
print(solution(g,p))