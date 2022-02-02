def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[0], reverse=True)
    now = routes[0][0]
    for route in routes[1:]:
        if now > route[1]:
            now = route[0]
            answer += 1
    return answer
