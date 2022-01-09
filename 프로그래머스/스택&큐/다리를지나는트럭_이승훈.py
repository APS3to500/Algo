from collections import deque

def solution(bridge_length, weight, truck_weights):
    move_on=[]
    wait=deque(truck_weights)
    while wait and move_on:
        first = wait.popleft()
        
    answer=[]
    return answer

# print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))