from collections import Counter, deque

def solution(k, tangerine):
    result = 0
    tangerine = Counter(tangerine)
    tangerine = sorted(tangerine.items(), key = lambda x:x[1], reverse = True)
    tangerine = deque(tangerine)
    # print(tangerine)
    
    while True:
        _, ea = tangerine.popleft()
        result += 1
        k -= ea
        
        if k <= 0:
            break
        
    return result