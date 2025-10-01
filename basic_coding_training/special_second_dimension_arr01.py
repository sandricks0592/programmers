def solution(n):
    answer = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        answer.append(row)
    return answer
n = 3
print(solution(n))

# 이차원 배열 만드는 법을 생각하기