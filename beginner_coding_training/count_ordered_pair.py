def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += 1
    return answer

n = 20
print(solution(n))
# 기억!! range()를 하면 0부터 시작이니 연산 실수갸 발생할 수 있다.