def solution(n):
    answer = 0
    for num in range(1,n+1):
        divisor = 0
        for i in range(1,num+1):
            if num % i == 0:
                divisor += 1
        if divisor >= 3:
            answer += 1
    return answer

n = 10
print(solution(n))

# 이중 for을 사용하여 숫자 하나씩의 약수의 갯수를 분석한다.