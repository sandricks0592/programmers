# 숫자로 이루어진 문자열 : t, p

def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p) + 1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
    return answer