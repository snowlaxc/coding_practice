from collections import deque

def solution(bandage, health, attacks):
    max_health = health
    health_time = 0
    
    time = 0
    attacks = deque(attacks)
    full_time = attacks[-1][0]
    
    for i in range(1, full_time + 1):
        time += 1
        
        monster = attacks.popleft()
        if monster[0] != time:
            attacks.appendleft(monster)
            health = min(max_health, health + bandage[1])
            health_time += 1
            
            if health_time == bandage[0]:
                health = min(max_health, health + bandage[2])
                health_time = 0
        else:
            health -= monster[1]
            health_time = 0
            if health <= 0:
                return -1
        
    return health