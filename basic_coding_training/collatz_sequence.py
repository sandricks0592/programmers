def solution(n):
    answer = []
    n = int(n)
    while n != 1:
        answer.append(int(n))
        if n%2 == 0:
            n = n/2
        elif n%2 == 1:
            n =  3*n+1
    answer.append(1)
    return answer

print(solution(10))

# int는 iterable이 아니라는걸 기억하고 1의 조건을 다시 생각해보고 1추가 기억하기