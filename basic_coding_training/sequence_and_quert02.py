# def solution(arr, queries):
#     answer = []    
#     for s,e,k in queries:
#         for i in range(len(arr)):
#             if s <= arr[i] <= e and arr[i] >= k:
#                 answer += min.arr[i]
#     return answer


def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        # s <= i <= e 범위의 arr[i] 중 k보다 큰 값만 추출
        candidates = [arr[i] for i in range(s, e+1) if arr[i] > k]
        
        if candidates:          # 후보가 있으면 최소값
            answer.append(min(candidates))
        else:                  # 없으면 -1
            answer.append(-1)
            
    return answer

# 