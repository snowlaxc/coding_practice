def solution(arr):
    answer = 0
    
    max_n = 1
    for a in arr:
        max_n *= a
    
    for i in range(arr[-1], max_n + 1):
        for j in arr:
            if i % j != 0:
                answer = 0
                break
            else:
                answer = i
        if answer != 0:
            return answer