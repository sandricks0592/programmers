def solution(board):
    n = len(board)
    # 위험지역 표시 배열 생성
    danger = [(0)*n for _ in range(n)]

    # 지뢰 주변 8방향 좌표 설정
    directions = [(-1,-1),(-1,0), (-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    # 지뢰와 주변 위험 지역 표시
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                danger[r][c] = 1 # 본인 포함
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        danger[nr][nc] = 1
    
    # 안전 지역 카운트
    safe_count = 0
    for r in range(n):
        for c in range(n):
            if danger[r][c] == 0:
                safe_count += 1
    
    return safe_count
