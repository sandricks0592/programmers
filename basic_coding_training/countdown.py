def solution(start_num, end_num):
    answer = []
    answer = list(range(start_num, end_num-1,-1))
    return answer


# range()는 숫자 시퀀스를 만들기 위해 필수적이고, 반복을 자동화 해준다.
# 또한 직접 일일이 쓰지 않아도 되니 코드의 간결성

def solution2(start_num, end_num):
    answer = []
    current = start_num        # 시작 숫자를 current에 저장
    for _ in range(start_num - end_num + 1):  # 반복 횟수 계산
        answer.append(current)  # 현재 숫자를 리스트에 추가
        current -= 1            # current를 1 감소
    return answer

print(solution(10, 3))
print(solution2(10, 3))
