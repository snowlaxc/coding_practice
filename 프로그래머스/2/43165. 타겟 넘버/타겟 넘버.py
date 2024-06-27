def solution(numbers, target):
    answer = 0
    len_n = len(numbers)
    
    def DFS(time, result):
        nonlocal answer
        if time != len_n:
            DFS(time+1, result+numbers[time])
            DFS(time+1, result-numbers[time])
        else:
            if result == target:
                answer += 1
    
    DFS(0, 0)
    return answer