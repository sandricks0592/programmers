def solution(quiz):
    answer = []
    for q in quiz:
        left, right = q.split(" = ")   # 왼쪽 식과 오른쪽 값으로 분리
        if eval(left) == int(right):   # 오른쪽 값은 문자열이므로 int로 변환
            answer.append('O')
        else:
            answer.append('X')
    return answer

quiz = ["3 - 4 = -3", "5 + 6 = 11"]
print(solution(quiz))

# 인덱스 보다는 left, right 변수 안에 넣어주고 두개의 타입을 맞춰주기