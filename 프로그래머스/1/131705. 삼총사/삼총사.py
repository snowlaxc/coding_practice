def solution(number):
    answer = 0
    len_number = len(number)
    
    for i in range(len_number):
        for j in range(i + 1, len_number):
            for k in range(j + 1, len_number):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer