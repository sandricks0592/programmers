def solution(arr, queries):
    answer = []    
    for s,e,k in queries:
        for i in range(len(arr)):
            if s <= arr[i] <= e and arr[i] >= k:
                answer += min.arr[i]
    return answer