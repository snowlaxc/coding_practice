def solution(k, score):
    hof = []
    announce_score = []
    for i in score:
        hof.append(i)
        hof.sort(reverse = True)
        if len(hof) <= k:
            announce_score.append(hof[-1])
        else:
            announce_score.append(hof[k-1])
        
    return announce_score