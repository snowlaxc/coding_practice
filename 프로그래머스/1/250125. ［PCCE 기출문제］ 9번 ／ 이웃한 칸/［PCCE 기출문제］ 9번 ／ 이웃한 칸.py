def solution(board, h, w):
    answer = 0
    board_len = len(board)
    color = board[h][w]
    
    if (h-1 >= 0) and (board[h-1][w] == color):
        answer += 1
    if (h+1 <= board_len-1) and (board[h+1][w] == color):
        answer += 1
    if (w-1 >= 0) and (board[h][w-1] == color):
        answer += 1
    if (w+1 <= board_len-1) and (board[h][w+1] == color):
        answer += 1

    return answer