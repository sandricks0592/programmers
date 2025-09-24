# def solution(arr, flag):
#     answer = []
#     for v,k in zip(arr, flag):
#         for i in range(len(flag)):
#             if k[i] == True:
#                 answer.extend([v]*(v*2))
#             else:
#                 answer.pop(k[-1])
#     return answer

def solution(arr, flag):
    answer = []
    for v, k in zip(arr, flag):
        if k:  # True일 때
            answer.extend([v] * (v*2))
        else:  # False일 때
            for _ in range(v):
                if answer:   # 리스트가 비어있지 않을 때만 제거
                    answer.pop()
    return answer


arr = [3, 2, 4, 1, 3]
flag = [True, False, True, False, False]
print(solution(arr, flag))