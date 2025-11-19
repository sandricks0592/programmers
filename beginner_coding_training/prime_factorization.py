# def solution(n):
#     answer = []
#     decimal = []
#     for num in range(1,n+1):
#         divisor = 0
#         for i in range(2,num+1) :
#             if num % i == 0:
#                 divisor += 1    
#     if divisor == 1:
#         decimal.append(i)
#     answer = decimal
#     return answer

def solution(n):
    answer = []
    
    # 2부터 n까지 반복하면서 나누어 떨어지는지 확인
    for i in range(2, n + 1):
        # i가 n의 약수일 때 계속 나눠지면 그 수는 소인수
        if n % i == 0:
            # i로 계속 나눠서 소인수인지 확인
            while n % i == 0:
                n //= i
            
            # 중복 없이 소인수 추가
            answer.append(i)
    
    return answer


n = 12
print(solution(n))

# if 안에 while을 사용하여 소인수인지 확인해보기