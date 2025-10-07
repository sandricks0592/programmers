# def solution(arr):
#     answer = [[]]
#     for r in arr:
#         for l in r:
#             if len(r) > len(l):
#                 while len(r) == len(l):
#                     l.append("0")
#             elif len(l) > len(r):
#                 while len(r) == len(l):
#                     r.append("0")
#             else:
#                 answer = arr
#         answer = arr
#     return answer

def solution(arr):
    rows = len(arr)            # 행의 수
    cols = max(len(r) for r in arr)  # 가장 긴 열의 길이

    # 목표 크기 = 행과 열 중 큰 값
    n = max(rows, cols)

    # 모든 행의 길이를 n으로 맞추기
    for row in arr:
        while len(row) < n:
            row.append(0)

    # 행의 개수를 n으로 맞추기
    while len(arr) < n:
        arr.append([0] * n)

    return arr


arr = [[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]
print(solution(arr))

# 행 열을 따로 생각하고 둘 중 최댓값을 선별해 각각 조건에 맞게 함수 적기