def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        answer = answer + str(i) * (food[i] // 2)
        
    answer = answer + str(0) + answer[::-1]
    
    return answer