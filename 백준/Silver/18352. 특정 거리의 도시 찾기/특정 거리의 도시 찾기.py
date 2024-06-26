import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
distance = [0] * (N+1)
visited = [False] * (N+1)

for m in range(M):
    src, ter = map(int, sys.stdin.readline().split())
    graph[src].append(ter)

def bfs(start):
    answer = []
    que = deque([start])
    visited[start] = True
    # distance[start] = 0
    while que:
        now = que.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                que.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == K:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end = '\n')

bfs(X)