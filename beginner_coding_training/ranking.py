# def solution(score):
#     answer = []
#     avg = []
#     for eng,math in score:
#         avg.append((eng+math)//2)
#     sorted_avg = sorted(avg, reverse = True)
#     for x in avg:
#         answer.append(sorted_avg.index(x)+1)
#     return answer

def solution(score):
    answer = []
    for eng,math in score:
        avg.append((eng+math)//2)
    
    return answer

# 85,85,65 일 경우 00, 0, 2로 계산해서 순위는 1, 1, 3이 나와 2등이 사라지는 오류가 발생한다.

score = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
print(solution(score))