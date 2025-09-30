def solution(arr, n):
    answer = []
    if len(arr) % 2 == 1:
        for i in range(len(arr)):
            if i % 2 == 0:
                answer.append(arr[i]+n)
            elif i % 2 == 1: 
                answer.append(arr[i])
    elif len(arr) % 2 == 0:
        for i in range(len(arr)):
            if i % 2 == 0:
                answer.append(arr[i])
            elif i % 2 == 1: 
                answer.append(arr[i]+n)
    return answer

arr = [49, 12, 100, 276, 33]
n = 27
print(solution(arr, n))