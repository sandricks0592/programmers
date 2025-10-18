def solution(balls, share):
    answer = 0
    a=b=c=1
    for i in range(1,balls+1):
        a *=i
    for e in range(1,balls-share+1):
        b *=e
    for j in range(1,share+1):
        c *=j
    answer = a // (b * c)
    return answer

balls = 3
share = 2
print(solution(balls, share))

# range 범위 설정 잘하기, 3개 변수 선언하는법 기억하기