from collections import deque

def solution(board, moves):
    n = len(board)
    m = len(board[0])
    result = [[0] * n for _ in range(m)]
    baguni = []
    answer = 0
    
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = board[i][j]
    result = [deque(b) for b in result]
    
    for move in moves:
        temp_deque = result[move-1]
        temp_doll = 0
        if temp_deque:
            while temp_doll == 0:
                temp_doll = result[move-1].pop()
                
        if temp_doll != 0:
            if baguni:
                if baguni[-1] == temp_doll:
                    baguni = baguni[:-1]
                    answer += 2
                else:
                    baguni.append(temp_doll)
            else:
                baguni.append(temp_doll)
                
        result[move-1] = temp_deque
    
    return answer