import string

def solution(s):
    input_s = list(s.lower())
    print(input_s)
    input_s[0] = input_s[0].upper()
    
    for i in range(0, len(input_s) - 1):
        if input_s[i] == ' ':
            input_s[i+1] = input_s[i+1].upper()
    
    answer = ''.join(input_s)
    
    return answer