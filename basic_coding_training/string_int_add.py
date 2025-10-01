def solution(num_str):
    answer = 0
    num_str = list(num_str)
    for i in num_str:
        answer += int(i)
    return answer

num_str = '123456789'
print(solution(num_str))