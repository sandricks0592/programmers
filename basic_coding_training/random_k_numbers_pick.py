# def solution(arr, k):
#     answer = []
#     for i in range(len(arr)):
#         if len(answer) == 0:
#             answer.append(arr[i])
#         else:
#             while len(answer) < k:
#                 if arr[i] != arr[i-1]:
#                     answer.append(arr[i])
#                 else:
#                     answer += '-1'
#     return answer

def solution(arr, k):
    answer = []
    for v in arr:
        if v not in answer:   # 아직 안 나온 수면 추가
            answer.append(v)
        if len(answer) == k:  # k개 채우면 멈춤
            break
    
    # 길이가 부족하면 -1로 채우기
    while len(answer) < k:
        answer.append(-1)
    
    return answer


arr = [0, 1, 1, 2, 2, 3]
k = 3
print(solution(arr, k))

# not in 사용 익숙해지기