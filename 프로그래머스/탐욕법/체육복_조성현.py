def solution(n, lost, reserve):
    answer = 0
    student = [1] * n
    for i in lost:
        student[i-1] -= 1
    for j in reserve:
        student[j-1] += 1
    for k in range(n):
        if student[k] == 0:
            if 0 <= k + 1 < n and student[k + 1] == 2:
                student[k + 1] -= 1
                student[k] += 1
            elif 0 <= k - 1 < n and student[k - 1] == 2:
                student[k - 1] -= 1
                student[k] += 1
        elif student[k] == 2:
            if 0 <= k + 1 < n and student[k + 1] == 0:
                student[k + 1] += 1
                student[k] -= 1
            elif 0 <= k - 1 < n and student[k - 1] == 0:
                student[k - 1] += 1
                student[k] -= 1
    answer = n - student.count(0)
    return answer

n=5
lost=[2, 4]
reserve =[1, 3, 5]
print(solution(n,lost,reserve))