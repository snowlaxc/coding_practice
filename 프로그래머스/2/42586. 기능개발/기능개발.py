from collections import deque, Counter

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    day = 0
    now_prg = 0
    now_spd = 0
    answer = []

    for _ in range(len(progresses)):
        now_prg = progresses.popleft()
        now_spd = speeds.popleft()
        now_prg += now_spd * day
        
        while True:
            if now_prg < 100:
                day += 1
                now_prg += now_spd
            else:
                answer.append(day)
                break
    print(answer)
    
    answer = sorted(Counter(answer).items(), key = lambda x:x[0], reverse = False)
    print(answer)
    
    answer = list(i[1] for i in answer)
    print(answer)
        
    return answer