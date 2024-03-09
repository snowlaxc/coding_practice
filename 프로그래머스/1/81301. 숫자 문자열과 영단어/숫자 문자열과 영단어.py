def solution(s):
    
    eng_digit = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    temp = []
    answer = []
    
    def temp_to_alp(temp):
        temp_alp = ''.join(temp)
        if temp_alp in eng_digit.keys():
            answer.append(str(eng_digit[temp_alp]))
            temp.clear()
        return temp
                
    
    for i in list(s):
        if i.isdecimal():
            if temp:
                temp = temp_to_alp(temp) 
            answer.append(i)
            
        else:
            temp.append(i)
        
        if temp:
            temp = temp_to_alp(temp)
                
            
    return int(''.join(answer))