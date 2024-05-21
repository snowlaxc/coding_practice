from collections import deque

def solution(n, words):
    words = deque(words)
    already = []
    
    now = words.popleft()
    already.append(now)
    
    end_alp = now[-1]
    rounds = 1
    time = 1
    
    while words:
        time += 1
        now = words.popleft()
        if time > n:
            time = 1
            rounds += 1
        if end_alp == now[0] and now not in already:
            already.append(now)
            end_alp = now[-1]
            
        else:
            return time, rounds
    
    return [0, 0]
    
    
        