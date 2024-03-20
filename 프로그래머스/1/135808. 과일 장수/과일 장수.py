from collections import deque

def solution(k, m, score):
    len_score = len(score)
    score.sort(reverse = True)
    score = deque(score)
    
    k = 0
    result = 0
    
    for _ in range(0, len_score // m):
        for _ in range(m):
            k = score.popleft()    
        result += (k * m)
        
    return result