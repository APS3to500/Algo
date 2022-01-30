def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[0], reverse=True)
    
    now = routes[0][0]
    for route in routes[1:]:
        if route[1] < now:
            now = route[0]
            answer += 1
                
    return answer + 1