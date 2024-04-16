import heapq

def solution(n, k, enemy):
    answer = 0
    latest = 0

    heap = []
    ## 무적권을 써서 회복하는 걸로
    for i, v in enumerate(enemy):
        n -= v
        heapq.heappush(heap, -v)
        # print(i, n, k, heap)
        if n < 0 :
            if k > 0:
                pre_v = -heapq.heappop(heap)
                n += pre_v #음수 전환후 회복
                k -= 1
                answer = i + 1
            else:
                answer = i 
                break
        else:
            answer = i + 1

    return answer