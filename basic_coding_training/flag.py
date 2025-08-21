def solution(a, b, flag):
    answer = 0
    if flag:
        answer = a+b
    else:
        answer = a-b
    return answer
print(solution(-4,7,'true'))

# 불리언 타입을 조건문에 불러올땐 바로 적용되는거 기억하기!
# 만약 문자열을 받고싶다면 .lower()나 .upper()로 대소문자 맞춰주기