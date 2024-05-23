def solution(keymap, targets):
    answer = []
    
    key_dict = {}
    for key in keymap:
        i = 1
        for k in key:
            if k in key_dict:
                key_dict[k] = min(key_dict[k], i)
            else:
                key_dict[k] = i
            i += 1
        
    for target in targets:
        result = 0
        
        for t in target:
            if t in key_dict:
                result += key_dict[t]
            else:
                result -= 9999999
        
        if result <= 0:
            answer.append(-1)
        else:
            answer.append(result)
        
    return answer