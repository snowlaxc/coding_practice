from itertools import combinations
from math import sqrt

def solution(nums):
    answer = 0
    
    for i in combinations(nums, 3):
        check = 0
        # print(i, sum(i))
        
        for j in range(2, int(sqrt(sum(i))) + 1):
            if sum(i) % j == 0:
                check = 1
                break
        
        if check == 0:
            print(i, sum(i))
            answer += 1
                
    return answer