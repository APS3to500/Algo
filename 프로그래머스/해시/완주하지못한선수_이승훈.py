def solution(participant, completion):
    completion.sort()
    participant.sort()
    answer = ''
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            answer=participant[i]
            break
    else:
        answer = participant[-1]
