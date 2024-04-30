import heapq
def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    # print(scoville)
    
    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        
        if first < K:
            count += 1
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, (first + (second * 2)))
        else:
            break
        
    return -1 if scoville[0] < K else count