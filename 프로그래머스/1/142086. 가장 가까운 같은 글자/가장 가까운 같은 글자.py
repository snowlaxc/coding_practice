def solution(s):
    len_s = len(s)
    dict_s = {}
    answer = []
    
    for n, i in enumerate(list(s)):
        if i not in dict_s.keys():
            answer.append(-1)
        else:
            answer.append(n - dict_s[i])
        
        dict_s[i] = max(dict_s.get(i, n), n)
    
    return answer