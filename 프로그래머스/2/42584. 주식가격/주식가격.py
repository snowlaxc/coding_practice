from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        price = prices.popleft()
        time = 0
        for q in prices:
            time += 1
            if price > q:
                break
        answer.append(time)
    return answer