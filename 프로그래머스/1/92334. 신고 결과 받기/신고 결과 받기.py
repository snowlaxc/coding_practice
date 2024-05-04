def solution(id_list, report, k):
    reported_list = {}
    answer = {}
    
    for ids in id_list:
        reported_list[ids] = 0
        answer[ids] = 0
    
    report = set(report)
    
    for rp in report:
        user, reported = rp.split()
        reported_list[reported] += 1
        
    for rp in report:
        user, reported = rp.split()
        
        if reported_list[reported] >= k:
            answer[user] += 1
        
    # print(list(answer.values()))
    
    return list(answer.values())