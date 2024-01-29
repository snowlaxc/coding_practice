def solution(n):
    half = n // 2 + 1
    answer = 0
    
    for i in range(1, half):
        sum = 0
        
        for j in range(i, half + 1):
            sum += j
            if sum == n:
                answer += 1
            if sum > n:
                break
            
    return answer + 1