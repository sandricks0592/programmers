# def solution(lines):
#     answer = 0
#     lines1 = []
#     lines2 = []
#     lines3 = []
#     for l in rang(len(lines)):
#         for i in range(lines[l][0],lines[l][1]+1):
#             lines.append(i)
#     answer = lines1

def solution(lines):
    answer = 0
    # 인덱스를 사용하기 위해 범위를 잡음
    board = [0] * 201

    # lines에서 하나씩 받아옴
    for start, end in lines:
        for i in range(start,end):
            board[i + 100] += 1
    
    #2개 이상 겹치는 부분의 길이
    for x in board:
        if x > 1:
            answer += 1

    return answer

lines = [[0, 1], [2, 5], [3, 9]]
print(solution(lines))

# 새로운 리스트를 만들고 lines 범위만큼 1씩 더하게 한다음 1 초과 횟수 측정하는 코드