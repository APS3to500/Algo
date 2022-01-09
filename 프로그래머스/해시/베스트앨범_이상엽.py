def solution(genres, plays):
    answer = []
    dic={}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]].append([plays[i],i])
        else : 
            dic[genres[i]] = [[plays[i],i]]

    genre_rank ={}
    for genre in dic.keys():
        songs = dic[genre]
        plays_sum = 0
        for song in songs:
            plays_sum+=song[0]
        genre_rank[genre] = plays_sum
    genre_rank = sorted(genre_rank.items(), key=lambda x: x[1],reverse=True)
    
    for genre in genre_rank:
        song_rank=sorted(dic[genre[0]], key=lambda x:(-x[0],x[1]))
        best_two = 0
        
        for song in song_rank:
            answer.append(song[1])
            best_two +=1
            if best_two == 2:
                break

    return answer