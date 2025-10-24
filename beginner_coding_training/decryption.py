def solution(cipher, code):
    answer = ''
    for i in range(code - 1, len(cipher), code):
        answer += cipher[i]
    return answer

cipher = "dfjardstddetckdaccccdegk"
code = 4
print(solution(cipher, code))

#  출력값의 시작점 고려하기