def solution(citations):
    citations.sort(reverse=True)
    lst = []
    for i in range(len(citations)):
        lst.append(min(i + 1, citations[i]))
    answer = max(lst)
    return answer
