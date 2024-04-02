def solution(tickets):
    
    # tickets = sorted(tickets, key = lambda x:(x[0], x[1]))
    target_len = len(tickets) + 1
    visited = [False] * (target_len - 1)
    answer = []
    
    def DFS(now, path):
            if len(path) == target_len:
                answer.append(path)
            
            else:
                for index, ticket in enumerate(tickets):
                    if (visited[index] == False) and (now == ticket[0]):
                        visited[index] = True
                        DFS(ticket[1], path + [ticket[1]])
                        visited[index] = False
    
    DFS("ICN", ["ICN"])
    # print(answer)
    answer.sort()
    
    return answer[0]