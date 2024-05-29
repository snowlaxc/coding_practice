from collections import deque

def solution(n, vertex):
    
    visited = [False] * (n+1)
    visited[0] = True
    visited[1] = True
    
    distance = [0] * (n+1)
    
    graph = [[] for _ in range(n+1)]
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    

    queue = deque([1])

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[v] + 1
    # print(distance)
    
    return distance.count(max(distance))