def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    double = ["ayaaya", "yeye", "woowoo", "mama"]
    
    for i in range(len(babbling)):
        for dou, c in zip(double, can):
            if dou in babbling[i]:
                babbling[i] = babbling[i].replace(dou, "double")
            if c in babbling[i]:
                babbling[i] = babbling[i].replace(c, " ")
        
        babbling[i] = babbling[i].replace(" ", "")
    print(babbling)
    
    return babbling.count('')