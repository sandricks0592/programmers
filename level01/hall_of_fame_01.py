# def solution(k, score):
#     answer = []
#     temp = []
#     for i in score:
#         temp.append(i)
#         if len(temp) <= 3:
#             answer += min(temp)
#         elif len(temp) >3:
#             temp = sorted(temp[,-2])
#             answer += temp.min()
#     return answer

def solution(k, score):
    answer = []
    temp = []  # 명예의 전당 점수들
    
    for s in score:
        temp.append(s)          # 점수 추가
        temp = sorted(temp, reverse=True)[:k]   # 상위 k명만 남기기
        answer.append(min(temp)) # 현재 명예의 전당 최하 점수 기록
    
    return answer


k = 3
score = [10, 100, 20, 150, 1, 100, 200]

print(solution(k, score))

# sorted(사용할 리스트, reverse = true)