def solution(n, arr1, arr2):
    answer = []
    
    binary = [1]
    for _ in range(n - 1):
        binary.append(binary[-1] * 2)
    binary.reverse()
    # print(binary)

    
    def make_map(num):
        return_map = []
        for k in binary:
            return_map.append(num // k)
            num = num % k
        return return_map
    
    map_1 = []
    map_2 = []
    
    for a, b in zip(arr1, arr2):
        map_1.append(make_map(a))
        map_2.append(make_map(b))
        answer.append("")
    
    # print(map_1)
    # print(map_2)
    
    for i in range(n):
        for j in range(n):
            if str(min(1, map_1[i][j] + map_2[i][j])) == "1":
                answer[i] += "#"
            else:
                answer[i] += " "
    # print(answer)
    
    return answer