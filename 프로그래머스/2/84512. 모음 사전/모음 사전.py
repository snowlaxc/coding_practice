def solution(word):
    dic = ['A', 'E', 'I', 'O', 'U']
    num = [1, 5, 25, 125, 625]
    answer = 0
    
    for i in range(len(word)-1,-1,-1):
        idx = dic.index(word[i])
        for j in range(5-i):
            answer += num[j]*idx
        answer += 1
        
    return answer

# A       1
# AA      1+1
# AAA     1+1+1
# AAAA    1+1+1+1
# AAAAA   1+1+1+1+1
# AAAAE   1+1+1+1+2
# AAAAI   1+1+1+1+3
# AAAAO   1+1+1+1+4
# AAAAU   1+1+1+1+5
# AAAE    1+1+1+(5+2)
# AAAEA   1+1+1+(5+2)+1
# AAAEE   1+1+1+(5+2)+2
# AAAEI   1+1+1+(5+2)+3
# AAAEO   1+1+1+(5+2)+4
# AAAEU   1+1+1+(5+2)+5
# AAAIA   1+1+1+(5+5+2)+1
