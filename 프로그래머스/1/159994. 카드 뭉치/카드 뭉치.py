def solution(cards1, cards2, goal):
    goal_dict = {}
    num = 0
    
    for i in goal:
        goal_dict[i] = num
        num += 1
    
    # print(goal_dict)
    
    result = "Yes"
    
    cards1 = [goal_dict.get(j, 999) for j in cards1]
    if cards1 != sorted(cards1, key = lambda x:x, reverse = False):
        result = "No"
        
    cards2 = [goal_dict.get(k, 999) for k in cards2]
    if cards2 != sorted(cards2, key = lambda x:x, reverse = False):
        result = "No"
    
    return result