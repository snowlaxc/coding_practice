from collections import deque

def solution(n, m, section):
    answer = 0
    
    section = deque(sorted(section))
    
    while section:
        min_sec = section.popleft()
        
        while section and (section[0] < min_sec + m):
            section.popleft()
        answer += 1
        
    return answer