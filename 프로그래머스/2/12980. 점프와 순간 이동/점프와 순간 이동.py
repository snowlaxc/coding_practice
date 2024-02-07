def solution(n):
    result = 0
    
    # 0에서 말고 N에서 부터 접근 (큰 숫자에서 2배를 해야 더 효율적이므로)
    while (n != 1):
        if (n % 2 == 0):    # 짝수일 경우(순간이동 할 경우)
            n = n//2
        else:    # 홀수일 경우(한칸 움직일 경우)
            n = n - 1
            result += 1
    
    return result + 1