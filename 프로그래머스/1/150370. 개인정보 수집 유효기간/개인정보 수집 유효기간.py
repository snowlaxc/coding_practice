def solution(today, terms, privacies):
    answer = []
    
    new_terms = {}
    for i in terms:
        a, b = i.split()
        new_terms[a] = int(b) * 28
    
    def change(day):
        year = int(day[2:4])
        month = int(day[5:7])
        day = int(day[8:10])
        new_day = year * 12 * 28 + month * 28 + day
        return int(new_day)
    
    today = change(today)
        
    new_privacies = {}
    for j, k in enumerate(privacies):
        c, d = k.split()
        c = change(c) + new_terms[d]
        
        if today >= c:
            answer.append(j + 1)
    
    return answer