from collections import deque
import math

def solution(n, k):
    k_nums = deque([1])
    while k_nums[0] <= 1000000:
        k_nums.appendleft(k_nums[0] * k)
    # print(k_nums)
    
    temp_n = str('')
    k_num = 0
    
    for _ in range(len(k_nums)):
        k_num = k_nums.popleft()
        # print(k_num)
        if n >= k_num:
            temp_n += str(n // k_num)
            n = n % k_num
        else:
            temp_n += str('0')
    # print(temp_n)
    
    number = [int(i) for i in str(temp_n).split('0') if i != '']
    # print(number)
    
    answer = 0
    
    for j in number:
        if j == 1:
            pass
        else:
            j_sqrt = int(math.sqrt(j))
            j_bool = True
            for k in range(2, j_sqrt + 1):
                if j % k == 0:
                    print(k)
                    j_bool = False
            if j_bool is True:
                answer += 1
            
    return answer