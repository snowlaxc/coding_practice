def solution(n):
    num_list = [1, 2, 3, 5]
    
    if n > 4:
        for i in range(4, n):
            num_list.append((num_list[i-2] + num_list[i-1]) % 1234567)
    
    return num_list[n-1]