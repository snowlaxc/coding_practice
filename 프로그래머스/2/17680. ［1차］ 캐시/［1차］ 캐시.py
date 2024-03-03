from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache_list = deque(["None"] * cacheSize)
    
    for i in cities:
        i = i.lower()
        
        if i in cache_list:
            answer += 1
            if cache_list:
                cache_list.remove(i)
                cache_list.append(i)
        else:
            answer += 5
            if cache_list:
                cache_list.popleft()
                cache_list.append(i)
            
        # print(cache_list)
            
    return answer
