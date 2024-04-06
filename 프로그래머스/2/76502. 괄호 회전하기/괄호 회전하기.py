def solution(s):
    answer = 0
    s = list(s)
    print(s)
    
    for _ in range(len(s)):
        temp = []
        for i in range(len(s)):
            if len(temp):
                if (temp[-1] == '[') and (s[i] == ']'):
                    temp.pop()
                elif (temp[-1] == '{') and (s[i] == '}'):
                    temp.pop()
                elif (temp[-1] == '(') and (s[i] == ')'):
                    temp.pop()
                else:
                    temp.append(s[i])
            else:
                temp.append(s[i])    
        if len(temp) == 0:
            answer += 1
        s.append(s.pop(0))
    
    return answer