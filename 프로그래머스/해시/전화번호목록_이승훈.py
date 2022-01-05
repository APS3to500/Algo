def solution(phone_book):
    phone_book.sort()
    mlen=0
    answer=True
    s=[]
    for i in range(len(phone_book)):
        t=phone_book[i]
        if len(t)>mlen:
            for j in s:
                if j == t[:len(j)]:
                    answer=False
                    break
            else:    
                s.append(t)
                mlen=len(t)
        else:
            s=[t]
            mlen=0
        if not answer:
            break
    return answer