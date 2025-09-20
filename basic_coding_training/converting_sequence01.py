def solution(arr):
    answer = []
    for i in range(len(arr)):
        if 100 >= arr[i] >= 50 and arr[i] % 2 == 0:
            arr[i] = int(arr[i]/2)
        elif arr[i] < 50 and arr[i] % 2 == 1:
            arr[i] = int(arr[i] * 2)
        
    answer = arr
    return answer

arr = [1, 2, 3, 100, 99, 98]
print(solution(arr))