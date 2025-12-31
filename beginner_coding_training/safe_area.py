# def solution(board):
#     answer = 0
#     total = len(board[0])*len(board)
#     answer = total
#     return answer

# board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
# print(solution(board))

# [[0, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 0], 
#  [0, 0, 1, 0, 0], 
#  [0, 0, 0, 0, 0]]

def solution(board):
    n = len(board)
    # 위험지역 표시용 배열
    danger = [[0]*n for _ in range(n)]

    # 8방향 좌표 변화
    directions = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1),         (0,1),
        (1,-1),  (1,0), (1,1)
    ]

    # 지뢰와 주변 위험 지역 표시
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                danger[r][c] = 1  # 자기 자신도 위험
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        danger[nr][nc] = 1

    # 안전 지역 카운트 (for문과 if문으로)
    safe_count = 0
    for r in range(n):
        for c in range(n):
            if danger[r][c] == 0:
                safe_count += 1

    return safe_count

# 안전지대 표준을 잡아두고 활용하여 사용하기 