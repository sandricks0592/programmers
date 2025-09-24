def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if len(answer) == 0:
            answer.append(arr[i])
        else:
            while len(answer) < k:
                if arr[i] != arr[i-1]:
                    answer.append(arr[i])
                else:
                    answer += '-1'
    return answer

arr = [0, 1, 1, 2, 2, 3]
k = 3
print(solution(arr, k))