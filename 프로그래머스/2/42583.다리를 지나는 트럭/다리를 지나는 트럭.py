from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    start = deque(truck_weights)
    ing = deque([int(0)] * bridge_length)
    
    ing_weight = 0
    
    end = deque([])
    
    while True:
    # for i in range(1, 150):
        
        if len(ing) != 0:
            out = ing.popleft()

            if out != 0:
                end.append(out)
                ing_weight -= out
                
        if len(start) != 0:
            truck = start.popleft()
            
            if (ing_weight + truck <= weight):
                ing.append(truck)
                ing_weight += truck
            else:
                start.appendleft(truck)
                ing.append(int(0))
                
        # print(i, '초: ', end, ing, start)
                
        answer += 1
        
        if len(end) == len(truck_weights):
            break
        
    return answer
