# # BFS
# def solution(numbers, target):
#     leaves = [0]
#     count = 0
    
#     for num in numbers:
#         temp = []
        
#         for leaf in leaves:
#             temp.append(leaf + num)
#             temp.append(leaf - num)
        
#         leaves = temp
        
#     for leaf in leaves:
#         if leaf == target:
#             count += 1
            
#     return count


# DFS
def solution(numbers, target):
    answer = 0
    
    def dfs(idx, result):
        if idx == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])
    
    dfs(0, 0)
    return answer