def solution(arr):
    answer = 1
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != arr[j][i]:
                answer = 0
    return answer

arr = [[5, 192, 33], [192, 72, 95], [33, 95, 999]]
print(solution(arr))

# n * n 배열이면 n은 len(arr)로 통일 시켜도 상관없다.