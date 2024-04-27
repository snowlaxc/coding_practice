from collections import Counter

def solution(X, Y):
    X = Counter(X)
    Y = Counter(Y)

    inter = X & Y
    answer = []
    for i in inter.elements():
        answer.append(i)
    
    answer.sort(reverse = True)
    
    if not answer:
        return "-1"
    elif answer[0] == "0":
        return "0"
    else:
        return ''.join(answer)