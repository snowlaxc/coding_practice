def solution(brown, yellow):
    entire = brown + yellow
    wh = []
    
    for i in range(1, (entire + 1) // 2 + 1):
        if entire % i == 0:
            if i <= int(entire//i):
                wh.append([i, int(entire//i)])
    
    print(wh)
    
    for j in wh:
        if (2 * (j[0] + j[1]) - 4) == brown:
            return [j[1], j[0]]