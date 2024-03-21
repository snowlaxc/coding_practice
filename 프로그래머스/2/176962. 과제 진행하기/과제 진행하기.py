def solution(plans):
    answer = []
    
    plans = sorted(plans, key = lambda x:x[1], reverse = False)
    time_table = []
    
    for i in plans:
        h, m = map(int, i[1].split(':'))
        time_table.append(h*60 + m)
    time_table.append(9999)
    
    remain_time = 0
    remain_work = []
    
    for j in range(len(plans)):
        have_time = int(time_table[j+1] - time_table[j])
        
        if int(plans[j][2]) <= have_time:
            have_time = (have_time - int(plans[j][2]))
            answer.append(plans[j][0])
            
            while (have_time > 0) and (remain_work):
                plus_work, need_time = remain_work.pop()
                
                if have_time >= need_time:
                    answer.append(plus_work)
                    have_time -= need_time
                else:
                    remain_work.append([plus_work, need_time - have_time])
                    have_time = 0
                
            remain_time += have_time
            
        else:
            remain_work.append([plans[j][0], int(plans[j][2]) - have_time])
            
    while remain_work:
        plus_work, need_time = remain_work.pop()
        answer.append(plus_work)
    
    return answer