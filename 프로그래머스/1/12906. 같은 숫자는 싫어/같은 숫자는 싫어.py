from collections import deque

def solution(arr):
    arr = deque(arr)
    answer = deque([])
    
    a = arr.popleft()
    answer.append(a)
    
    b = arr.popleft()
    
    while True:
        if a != b:
            answer.append(b)
            a = b
        else:
            b = arr.popleft()
        
        if len(arr) == 0:
            if answer[-1] != b:
                answer.append(b)
            break
    
    return list(answer)
