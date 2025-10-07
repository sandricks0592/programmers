def solution(n):
    answer = []
    basic = [[0]*n for _ in range(n)]

    for i in range(basic[0][0],basic[0][n-1]):
        i += 1
    

    return basic

n = 4
print(solution(n))