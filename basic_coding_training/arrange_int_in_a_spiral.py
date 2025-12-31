# def solution(n):
#     answer = []
#     basic = [[0]*n for _ in range(n)]

#     for i in range(basic[0][0],basic[0][n-1]):
#         i += 1
    

#     return basic

def solution(n):
    answer = [[None for j in range(n)] for i in range(n)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x, y, m = 0, 0, 0
    for i in range(1, n**2 + 1):
        answer[y][x] = i
        if y + move[m][0] >= n or x + move[m][1] >= n or answer[y + move[m][0]][x + move[m][1]]:
            m = (m + 1) % len(move)
        y, x = y + move[m][0], x + move[m][1]
    return answer

n = 4
print(solution(n))