def solution(n, computers):
    
    answer = 0
    visited = [False for _ in range(n)]
    
    for i in range(n):
        if visited[i] == False:
            DFS(n, computers, i, visited)
            answer += 1

    return answer


def DFS(n, computers, i, visited):
    visited[i] = True
    
    for j in range(n):
        if (j != i) and (computers[i][j] == 1):
            if visited[j] == False:
                DFS(n, computers, j, visited)