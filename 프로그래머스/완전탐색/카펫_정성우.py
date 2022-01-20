def solution(brown, yellow):
    carpet=brown+yellow
    answer=[]
    for i in range(1,yellow+1):
        if yellow%i==0:
            yellow_x = yellow //i
            yellow_y = i
            if (yellow_x+2)*(yellow_y+2)==carpet:
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                return answer