def solution(arr, query):
    answer = []
    for i in range(len(query)):
        if i % 2 == 0:  # 짝수 번째 쿼리면 뒤 자르기
            arr = arr[:query[i]+1]
        else:           # 홀수 번째 쿼리면 앞 자르기
            arr = arr[query[i]:]
    answer = arr
    return answer


arr = [0, 1, 2, 3, 4, 5]	
query = [4, 1, 2]
print(solution(arr, query))