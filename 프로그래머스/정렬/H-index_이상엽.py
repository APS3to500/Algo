def solution(citations):
    citations.sort(reverse=True)
    for idx in range(len(citations)):
        if idx >= citations[idx]:
            return idx
    return len(citations)