def solution(numbers):
    answer = []
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            # print(i,j)
            answer.append(numbers[i]+numbers[j])
            
    answer = list(set(answer))
    answer.sort(reverse = False)
    
    return answer