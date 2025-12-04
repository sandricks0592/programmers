def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    return answer[::-1]

n = 12345
print(solution(n))

# 그냥 나열하고 슬라이스 이용하기