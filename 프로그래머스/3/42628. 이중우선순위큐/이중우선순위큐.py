from heapq import heapify, heappush, heappop

def solution(operations):
    answer = []
    hqueue = []
    
    for i in operations:
        if i == "D -1":
            if hqueue:
                heappop(hqueue)
        elif i == "D 1":
            if hqueue:
                hqueue.sort()
                hqueue.pop()
        else:
            _, num = i.split(" ")
            num = int(num)
            heappush(hqueue, num)

    return [max(hqueue), min(hqueue)] if hqueue else [0, 0]