def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
    # print(dp)
    
    return dp[-1] % 1234567

# def solution(n):
#     fibo_list = [0, 1]
    
#     for _ in range(n - 1):
#         fibo_list.append(fibo_list[-1] + fibo_list[-2])
        
#     return fibo_list[n] % 1234567