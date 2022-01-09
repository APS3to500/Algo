from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    wait=deque(truck_weights)
    ongoing=deque()
    bridge=deque()
        
    while wait or bridge:
        time+=1
        if wait and wait[0]+sum(bridge)<=weight and bridge_length>=len(bridge):
            bridge.append(wait.popleft())
            ongoing.append(0)
            
        for i in range(len(ongoing)):
            ongoing[i]+=1
            
        if ongoing[0]>=bridge_length:
            ongoing.popleft()
            bridge.popleft()
            
    # while문을 탈출하면 시간을 1 더해줘야함
    return time+1