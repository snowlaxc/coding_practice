from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    len_n = len(numbers)
    num_list = set()

    for i in range(1, len_n+1):
        for j in permutations(numbers, i):
            num_list.add(int(''.join(j)))
        
    answer = 0
    # print(num_list)
    
    for n in num_list:
        yn = True
        if n > 1:
            for m in range(2, int(n**0.5)+1):
                if n % m == 0:
                    yn = False
            if yn == True:
                answer += 1
    
    return answer