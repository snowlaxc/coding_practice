from collections import deque

def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0, 0))    # 시작
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            height = len(maps)
            width = len(maps[0])
            
            if (height > nx >= 0) and (width > ny >= 0) and (maps[nx][ny] == 1):
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    answer = maps[height-1][width-1]

    if answer == 1:
        answer = -1
    return answer