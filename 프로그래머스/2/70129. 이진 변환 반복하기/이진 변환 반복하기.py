def solution(s):
    s = list(s)
    
    repeat = 0
    count = 0
    
    while s != ["1"]:
        
        new = []
        
        for i in s:
            if i == "1":
                new.append(i)
            else:
                count += 1

        s = list(bin(len(new)))
        s = s[2:]
        
        repeat += 1
                    
    return [repeat, count]