from collections import Counter

def solution(want, number, discount):
    answer = 0
    need = {}    
    for w, n in zip(want, number):
        need[w] = n
    
    total = sum(number)
    day = len(discount)
    
    for i in range(day - total + 1):
        temp = Counter(discount[i:i+total])
        if need == temp:
            answer += 1

    return answer