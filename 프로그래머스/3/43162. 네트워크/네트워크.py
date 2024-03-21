def solution(n, computers):
    answer = 0
    visited = [False] * n
            
    def DFS(now):
        visited[now] = True
        
        for nxt in range(n):
            if (nxt != now):
                if (computers[now][nxt] == 1):
                    if (visited[nxt] == False):
                        DFS(nxt)
                
    for now in range(n):
        if visited[now] == False:
            DFS(now)
            answer += 1
    
    return answer