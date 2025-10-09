def solution(n):
    answer = 0
    sum  = n
    if n % 6 == 0:
        answer = n // 6
    else:
        while sum % 6 != 0:
            sum += n
        answer =  sum // 6
    return answer

n = 10
print( solution(n))