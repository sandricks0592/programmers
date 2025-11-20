def solution(board):
    answer = 0
    total = len(board[0])*len(board)
    answer = total
    return answer

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
print(solution(board))

[[0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0], 
 [0, 0, 1, 0, 0], 
 [0, 0, 0, 0, 0]]