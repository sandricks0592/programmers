def solution(arr):
    n = len(arr)
    # 목표 크기: n보다 크거나 같은 가장 가까운 2의 거듭제곱
    target = 1
    while target < n:
        target *= 2
    
    # 부족한 만큼 0 추가
    arr += [0] * (target - n)
    return arr


arr = [1, 2, 3, 4, 5, 6]
print(solution(arr))