import math

def solution(number, limit, power):
    answer = 0
    
    for knight in range(1, number + 1):
        # print(knight, int(math.sqrt(knight)))
        
        if knight == 1:
            weapon = 1
        
        if (knight == 2) or (knight == 3):
            weapon = 2
        
        if knight > 3:
            weapon = 0
            for i in range(2, int(math.sqrt(knight)) + 1):
                if knight % i == 0:
                    weapon += 1
            if math.sqrt(knight) % 1 == 0:
                weapon = (weapon - 1) * 2 + 1
            else:
                weapon = weapon * 2
            weapon += 2
        
        if weapon > limit:
            weapon = power
        answer += weapon
        # print(weapon)
        
    return answer