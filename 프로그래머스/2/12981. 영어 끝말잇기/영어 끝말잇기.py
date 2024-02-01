def solution(n, words):
    time = 0
    before = words[0][0]
    done = []
    
    error = 0
    result = [0,0]
    
    for _ in range(len(words)):
        time += 1
        i = words.pop(0)
        
        if before == i[0]:
            before = i[-1]
        else:
            error = 1
            break
        
        if i not in done:
            done.append(i)
        else:
            error = 1
            break
            
    if error == 1:
        result = [int(time % n), int((time + (n - 1)) // n)]
        
        if result[0] == 0:
            result[0] = n
            
    return result