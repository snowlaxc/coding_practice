from collections import deque

def solution(s):
    s = deque(s)
    
    first_alp = s.popleft()
    # print(first_alp)
    first = 1
    other = 0
    answer = 0
    debug = 1
    
    for i in range(len(s)):
        if (first == other):
            # print(debug)
            answer += 1
            other = 0
            if s:
                first = 1
                first_alp = s.popleft()
                debug += 1
                # print(first_alp)
            else:
                return answer
        else:
            if s:
                next_alp = s.popleft()
                debug += 1
                # print(next_alp)
            else:
                # print(debug)
                answer += 1
                break
                
            if first_alp != next_alp:
                other += 1
            else:
                first += 1

    return answer + 1