from collections import deque, Counter

def solution(want, number, discount):
    junghyeon = {}
    need_day = sum(number)
    full_day = len(discount)
    discount_list = []
    result = 0
    
    for a, b in zip(want, number):
        junghyeon[a] = b
        
    discount_count = Counter(discount)
    
    for i in want:
        if discount_count[i] < junghyeon[i]:
            return result
        
    # print(junghyeon)
    # print(discount_count)
    
    for j in range(0, (full_day) - need_day + 1):
        discount_list.append(Counter(discount[j:j + need_day]))
    
    for k in discount_list:
        if k == junghyeon:
            result += 1
    return result