def solution(n):
    
    ### 3진법으로 변환
    three_ten = []
    base3 = [1]
    
    while base3[-1] * 3 <= n:
        base3.append(base3[-1] * 3)
    
    base3.reverse()
    print(base3)
        
    for i in base3:
        if n >= i:
            three_ten.append(n // i)
            n = (n % i)
        else:
            three_ten.append(0)
            
    ### 3진법 앞뒤로 뒤집기
    three_ten.reverse()
    print(three_ten)
    
    ### 10진법으로 다시 전환
    answer = 0
    
    for a, b in zip(base3, three_ten):
        answer += (a * b)
    print(answer)
    
    return answer