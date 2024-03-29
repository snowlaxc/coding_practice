def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
    
    def dfs(k, count, dungeons, visited):
        nonlocal answer
        answer = max(answer, count)
        
        for i in range(len(dungeons)):
            if (visited[i] == False) and (k >= dungeons[i][0]):
                visited[i] = True
                dfs(k - dungeons[i][1], count + 1, dungeons, visited)
                visited[i] = False    # 백트레킹
                
    dfs(k, 0, dungeons, visited)
        
    return answer