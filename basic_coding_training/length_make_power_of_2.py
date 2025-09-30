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

# *=를 사용해서 2의 거듭제곱 취급하는걸 생각하고, 리스트 길이도 따로 분리해서 생각하기