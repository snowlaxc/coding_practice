from collections import Counter

def solution(N, stages):
    all_users = len(stages)
    stages_temp = dict(Counter(stages))
    fail_user = {}
    for i in range(1, N+2):
        fail_user[i] = stages_temp.get(i, 0)
    # print(fail_user)
    
    challenge_user = {}
    for stage, failed in fail_user.items():
        challenge_user[stage] = all_users
        all_users -= failed
    # print(challenge_user)
    
    fail_perc = {}
    for i in range(1, N+1):
        if challenge_user[i] == 0:
            fail_perc[i] = 0
        else:
            fail_perc[i] = fail_user[i]/challenge_user[i]
    # print(fail_perc)
    
    fail_perc = sorted(fail_perc.items(), key = lambda x:x[1], reverse = True)
    # print(fail_perc)
    
    return [i[0] for i in fail_perc]