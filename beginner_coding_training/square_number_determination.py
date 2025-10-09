def solution(n):
    answer = 0
    if int(n**0.5) == n**0.5:
        answer = 1
    else:
        answer = 2
    return answer

n = int(input())
print(solution(n))

# 타입 구별하는거 기억하기. 값은 같아도 타입은 다를수도 있다.