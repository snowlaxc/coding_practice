def solution(n):
    result = 0
    
    while (n != 1):
        if (n % 2 == 0):
            n = int(n/2)
        else:
            n = n - 1
            result += 1
    
    return result + 1