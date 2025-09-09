def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        for i in range(s, e+1):   # s ≤ i ≤ e
            if i % k == 0:        # 인덱스 i가 k의 배수라면
                arr[i] += 1
    answer = arr
    return answer

# range() 좀 더 잘 활용하기

arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 1],[0, 3, 2],[0, 3, 3]]

print(solution(arr,queries))