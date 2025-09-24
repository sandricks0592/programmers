# def solution(arr):
#     answer = []
#     for i in range(len(arr)):
#         while arr[i] > 0:
#             answer.append(arr[i])
#     return answer

def solution(arr):
    answer = []
    for num in arr:
        answer.extend([num] * num)
    return answer


arr = [5, 1, 4]
print(solution(arr))

# append()는 리스트 끝에 x라는 하나의 요소를 추가하지만 extend()는 각각의 요소로 추가한다.
