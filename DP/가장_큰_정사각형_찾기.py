def solution(board):
    answer = 0

    x = len(board)
    y = len(board[0])
    answer = 0

    for i in range(1, x): # row 하나일때는, 확인하지 못한다
        for j in range(1, y):
            if board[i][j]:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                if answer <= board[i][j]:
                    answer = board[i][j]
                else:
                    answer = 1


    if answer == 0:
        for j in range(y):
            if board[0][j]:
                answer = 1
                break


    return answer * answer

print(solution([[0,0,1,1]]))