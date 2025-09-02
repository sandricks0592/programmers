def solution(arr, k):
    answer = []
    if k%2 == 1:
        answer = [i * k for i in arr]
    elif k%2 == 0:
        answer = [i + k for i in arr]
    return answer

arr = [1, 2, 3, 100, 99, 98]
k = 3
print(solution(arr,k))