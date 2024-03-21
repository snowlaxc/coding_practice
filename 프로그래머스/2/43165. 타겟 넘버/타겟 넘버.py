def solution(numbers, target):
    global answer
    answer = 0
    
    DFS(numbers, target, 0, 0)
    return answer

def DFS(numbers, target, time, result):
    if (len(numbers) == time):
        if (target == result):
            global answer
            answer += 1
    else:
        DFS(numbers, target, time + 1, result + numbers[time])
        DFS(numbers, target, time + 1, result - numbers[time])