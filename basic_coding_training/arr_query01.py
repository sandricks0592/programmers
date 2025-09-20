# def solution(arr, queries):
#     answer = []
#     new_arr = []
#     for s,e in queries:
#         for i in range(len(arr)):
#             for a in range(len(queries)):
#                 if s[i] <= arr[a] <= e[i]:
#                     answer = arr[:a] + arr[a]+1 + arr[a+1:]
#     return answer

def solution(arr, queries):
    answer = []
    for s,e in queries:
        for i in range(s,e+1):
            arr[i] += 1
    answer = arr
    return answer

arr = [0, 1, 2, 3, 4]
queries = [[0, 1],[1, 2],[2, 3]]
print(solution(arr, queries))

# 배열을 통으로만 생각하지 말고 요소 하나하나를 사용할 수 있음을 생각하자.