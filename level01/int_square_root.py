def solution(n):
    answer = -1
    i = int(n**0.5)
    if i ** 2 == n:
        answer = (i+1) ** 2
    return answer

n = 121

print(solution(n))

# 제곱근은 식이 따로 없어서 ** 0.5 기억해서 활용하기