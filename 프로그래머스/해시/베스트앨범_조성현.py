
def solution(genres, plays):
    result = []
    line = {}
    answer = {}
    for i in range(len(genres)):
        if genres[i] in answer:
            answer[genres[i]] += plays[i]
            line[genres[i]].append((i,plays[i]))
        else:
            answer[genres[i]] = plays[i]
            line[genres[i]] = [(i,plays[i])]

    sorted_answer = sorted(answer, key=lambda item: item[1],reverse=True)
    for i in line:
        line[i] = sorted(line[i], key=lambda item:item[0],reverse=True)

    for i in range(len(sorted_answer)):
        if
        for j in range(2):
            result.append(sorted_answer[i][j])

    return result

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))