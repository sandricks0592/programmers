def solution(arr, queries):
    answer = []
    for i,j in queries:
        arr[i],arr[j] = arr[j],arr[i]
        answer = arr
    return answer

# for문을 쪼개서 사용 할 수 있다는거 기억하기
