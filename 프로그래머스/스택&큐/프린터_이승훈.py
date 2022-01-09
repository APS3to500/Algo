from collections import deque

def solution(priorities, location):
    target = priorities[location]
    new_priorities = deque()

    dec_location=0
    for idx,priority in enumerate(priorities):
        if priority >= target:
            new_priorities.append(priority)
        else:
            if idx<location:
                dec_location+=1
    location-=dec_location

    print(new_priorities,location)
    time=0
    while new_priorities:
        cur=new_priorities[0]
        for idx,priority in enumerate(new_priorities):
            if cur < priority:
                cur = priority
                new_priorities=list(new_priorities)
                new_priorities=deque(new_priorities[idx:] + new_priorities[:idx])
                if location>=idx:
                    location-=idx
                else:
                    location=len(new_priorities)+location-idx
        time+=1
        print(new_priorities,location)
        if location==0:
            return time
        else:
            new_priorities.popleft()
            location-=1
print(solution([1, 1, 9, 1, 1, 1],0))