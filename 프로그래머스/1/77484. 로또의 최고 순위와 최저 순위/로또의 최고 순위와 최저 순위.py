def solution(lottos, win_nums):
    max_win = 7
    min_win = 7
    
    for i in lottos:
        if i in win_nums:
            max_win -= 1
            min_win -= 1
        if i == 0:
            max_win -= 1
            
    return [min(6, max_win), min(6, min_win)]