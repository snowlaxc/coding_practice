def solution(elements):
    length = len(elements)
    elements += elements
    answer = []
    now = 0
    print(elements)
    
    for i in range(0, length + 1):
        now = elements[i]
        answer.append(now)
        for j in range(1, length):
            now += elements[i+j]
            answer.append(now)
            
    return len(set(answer))