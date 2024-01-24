from heapq import heapify, heappop, heappush

def solution(n, works):
    if n > sum(works):
        return 0
    
    works = [-w for w in works]
    heapify(works)
    
    for _ in range(n):
        a = heappop(works)    # 최소값 pop
        heappush(works, a + 1)  # 삽입
    
    result = 0
    
    for i in works:
        result += i*i
        
    return result
    
        
# def solution(n, works):
    
#     if n > sum(works):
#         return 0
    
#     while n != 0:
#         max_index = works.index(max(works))
        
#         if works[max_index] == 0:
#             break
            
#         else:
#             works[max_index] -= 1
#             n -= 1
        
#     result = 0
#     for i in works:
#         result += i*i
        
#     return result