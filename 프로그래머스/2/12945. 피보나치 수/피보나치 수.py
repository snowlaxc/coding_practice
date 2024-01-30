def solution(n):
    fibo_list = [0, 1]
    
    for _ in range(n - 1):
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
        
    return fibo_list[n] % 1234567