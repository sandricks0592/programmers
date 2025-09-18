def solution(str1, str2):
    answer = 0
    if str1 in str2:
        answer = 1
    else:
        answer = 0
    return answer

str1 = "abc"
str2 = "aabcc"
print(solution(str1, str2))