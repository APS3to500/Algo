def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        head = phone_book[i]
        for j in range(len(phone_book)):
            if i == j:
                continue
            if head == phone_book[j][0:len(head)]:
                answer = False
                return answer
    return answer


print(solution(["119", "97674223", "1195524421"]))