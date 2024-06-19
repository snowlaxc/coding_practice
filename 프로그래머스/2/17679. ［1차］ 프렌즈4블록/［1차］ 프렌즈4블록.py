def solution(m, n, board):
    answer = 0
    
    board = [list(row) for row in board]
    board = list(map(list, zip(*board[::-1])))
    
    while True:
        del_list = set()
        for i in range(n-1):
            for j in range(m-1):
                temp = board[i][j]
                if temp != '-' and temp == board[i][j+1] and temp == board[i+1][j] and temp == board[i+1][j+1]:
                    del_list.add((i, j))
                    del_list.add((i+1, j))
                    del_list.add((i, j+1))
                    del_list.add((i+1, j+1))

        del_list = sorted(del_list, key = lambda x:(x[0],x[1]), reverse = True)

        if del_list:
            answer += len(del_list)
            for (x, y) in del_list:
                del board[x][y]
                board[x].append('-')
        else:
            break
    
    return answer