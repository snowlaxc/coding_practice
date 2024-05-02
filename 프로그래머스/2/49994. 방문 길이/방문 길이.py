def solution(dirs):
    ctrl = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = (0, 0)
    answer = set()
    
    for i in dirs:
        nx, ny = ctrl[i]
        
        if (-5 <= x+nx <= 5) and (-5 <= y+ny <= 5):
            answer.add(((x, y), (x+nx, y+ny)))
            answer.add(((x+nx, y+ny), (x, y)))
            x += nx
            y += ny
    
    return len(answer)//2