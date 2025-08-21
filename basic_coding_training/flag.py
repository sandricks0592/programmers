def solution(a, b, flag):
    answer = 0
    if flag.lower() == 'true':
        answer = a+b
    else:
        answer = a-b
    return answer
print(solution(-4,7,'True'))