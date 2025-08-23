def solution(my_string, is_prefix):
    answer = 0
    if my_string.startswith(is_prefix):
        answer = 1
    else :
        answer = 0
    return answer

print(solution("banana","ba"))

# 파이썬 문자열 내장 메서드 startswith() 