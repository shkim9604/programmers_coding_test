def solution(board):
    answer = 0
    warning_loc = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                for a in warning_loc:
                    if i+a[0] > len(board[0])-1 or i+a[0] < 0:
                        continue
                    if j+a[1] > len(board[0])-1 or j+a[1] < 0:
                        continue
                    if board[i+a[0]][j+a[1]] == 1:
                        continue
                    board[i+a[0]][j+a[1]] = 'x'
    for i in board:
        answer += i.count(0)
    return answer