def solution(angle):
    if angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle == 180:
        answer = 4
    elif 90<angle<180:
        answer = 3
    else:
        return 0
    return answer

angle = 70
print(solution(angle))