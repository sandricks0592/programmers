def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                answer += board[i][j]
    return answer

board = [[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]]	
k = 2
print(solution(board, k))

# 이차원 배열을 쓸때는 이중 for문을 써야 한다.