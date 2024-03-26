from math import sqrt

def solution(n):
    answer = 0
    n_list = [True] * (n + 1)
    n_list[0] = False
    n_list[1] = False
    
    for i in range(2, n + 1):
        if n_list[i] == True:
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    # print(i, j)
                    for k in range(i, n + 1, i):
                        n_list[k] = False
                    break
        if n_list[i] == True:
            answer += 1
    
    return answer