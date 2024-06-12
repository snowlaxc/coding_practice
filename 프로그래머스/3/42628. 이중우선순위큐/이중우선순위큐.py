import heapq

def solution(operations):
    maxhq = []
    minhq = []
    
    for operation in operations:
        di, num = operation.split(" ")
        num = int(num)
        
        if di == "I":
            heapq.heappush(minhq, num)
            heapq.heappush(maxhq, -num)
            
        else:
            if minhq:
                if num == 1:
                    temp = -1 * heapq.heappop(maxhq)
                    minhq.remove(temp)
                else:
                    temp = -1 * heapq.heappop(minhq)
                    maxhq.remove(temp)
            
    if minhq:
        return [max(minhq), min(minhq)]
    return [0, 0]