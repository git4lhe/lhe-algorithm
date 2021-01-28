def solution(board, moves):
    # 00000
    # 00103
    # 02501
    # 42442
    # 35131
    answer = 0
    stack = []
    for j in moves:
        for i in range(len(board)):
            if board[i][j-1] != 0:
                stack.append(board[i][j-1])
                board[i][j-1] = 0

                if len(stack) >= 2:
                    if (stack[-1] == stack[-2]):
                        stack.pop()
                        stack.pop()
                        answer += 2

                break

    return answer