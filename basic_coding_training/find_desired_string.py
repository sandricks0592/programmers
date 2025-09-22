def solution(myString, pat):
    answer = 0
    if pat.upper() in myString.upper():
        answer = 1
    else:
        answer = 0
    return answer

myString = "AbCdEfG"
pat = "aBc"
print(solution(myString, pat))

# string.upper() 형식을 기억하기