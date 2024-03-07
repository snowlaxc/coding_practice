def solution(s):
    answer = []
    
    s = s.replace('{', '[')
    s = s.replace('}', ']')
    s = eval(s)
    
    s = sorted(s, key = lambda x:len(x), reverse = False)
    
    # print(s)
    
    for i in s:
        for j in i:
            if j not in answer:
                answer.append(j)
    
    return answer