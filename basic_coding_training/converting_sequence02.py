def solution(arr):
    answer = 0
    while True:
        prev = arr.copy()
        for i in range(len(arr)):
            if 100 >= arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
            elif 50 > arr[i] and arr[i] % 2 == 1:
                arr[i] = arr[i] *2 + 1
        answer += 1
        if arr == prev:
            return answer -1     
    

arr = [1, 2, 3, 100, 99, 98]
print(solution(arr))

#   prev는 이전 단계의 배열 상태를 저장하는 변수, arr.copy()를 쓰면 arr과 내용은 같지만 별도의 새로운 리스트를 만들어서 prev에 저장한다.