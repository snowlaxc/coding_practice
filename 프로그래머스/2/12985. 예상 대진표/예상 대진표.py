def solution(n,a,b):
    answer = 1
    
    while True:
        num_list = []
        i = n // 2
        for j in range(1, i+1):
            num_list.append(j)
            num_list.append(j)

        if num_list[a-1] == num_list[b-1]:
            return answer
        else:
            if a % 2 == 1:
                a += 1
            if b % 2 == 1:
                b += 1
            a = a // 2
            b = b // 2
            n = n // 2
            answer += 1
    