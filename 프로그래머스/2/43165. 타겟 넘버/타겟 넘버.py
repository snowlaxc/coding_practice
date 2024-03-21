def solution(numbers, target):
    answer = 0
    len_numbers = len(numbers)
    
    def DFS(time, result):
        if time != len_numbers:
            DFS(time + 1, result + numbers[time])
            DFS(time + 1, result - numbers[time])
        else:
            if result == target:
                nonlocal answer
                answer += 1
        
    DFS(0, 0)
    
    return answer