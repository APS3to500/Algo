def solution(bridge_length, weight, truck_weights):
    answer = 0
    Q = [0] * bridge_length
    
    while Q:
        answer += 1
        Q.pop(0)
        if truck_weights:
            if sum(Q) + truck_weights[0] <= weight:
                Q.append(truck_weights.pop(0))
            else:
                Q.append(0)
    return answer