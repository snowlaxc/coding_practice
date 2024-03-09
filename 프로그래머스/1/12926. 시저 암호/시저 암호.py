import string

def solution(s, n):
    answer = []
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    
    
    for i in s:
        if i in upper:
            answer.append(upper[(upper.index(i) + n) % len(upper)])
        elif i in lower:
            answer.append(lower[(lower.index(i) + n) % len(lower)])
        else:
            answer.append(i)
            
    answer = ''.join(answer)
    
    return answer