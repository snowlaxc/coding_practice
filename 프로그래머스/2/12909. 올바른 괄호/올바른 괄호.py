from collections import deque, Counter
def solution(s):
    s = deque(s)
    s_dict = Counter(s)
    
    if s_dict["("] != s_dict[")"]:
        return False
    
    for _ in range(len(s)):
        output = s.popleft()
        s_dict[output] -= 1
        if s_dict["("] > s_dict[")"]:
            return False
    
    return True