from collections import deque

def solution(bandage, health, attacks):
    max_health = health
    
    time = 0    # 총 라운드 (마지막 공격 시간)
    full_time = attacks[-1][0]   # 추가 회복 가능 시전 시간
    health_time = 0    # 연속 회복 시전 시간
    
    attacks = deque(attacks)    # attacks 덱으로 생성
    
    for i in range(1, full_time + 1):
        time += 1
        monster = attacks.popleft()
        
        if monster[0] != time:    # 몬스터가 공격하지 않아 회복할 경우
            attacks.appendleft(monster)    # 원상복귀
            health = min(max_health, health + bandage[1])    # 회복
            health_time += 1
            
            if health_time == bandage[0]:    # 추가 회복 가능 시
                health = min(max_health, health + bandage[2])
                health_time = 0    # 연속 회복 시전 시간 초기화
        else:
            health -= monster[1]    # 몬스터가 공격할 경우
            health_time = 0    # 연속 회복 시전 시간 초기화
            if health <= 0:    # 사망할 경우
                return -1
        
    return health