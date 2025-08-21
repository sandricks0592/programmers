def solution(numbers,n):
    answer = 0
    for i in range(len(numbers)):
        if answer <= n:
            answer += numbers[i]
        elif answer > n:
            print(answer)
            return answer 
    return answer
# return 0은 함수 종료되는 순간  무조건 0을 반환하면서 answer가
# 얼마였는지는 상관없이 버려지니까  주의하기!