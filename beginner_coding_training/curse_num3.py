def solution(n):
    answer = 0
    arr= []
    for i in range(1,1000):
        if '3' not in str(i) and i % 3 != 0:
            arr.append(i)
    answer = arr[n-1]
    return answer

n = 15
print(solution(n))