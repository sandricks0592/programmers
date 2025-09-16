# def solution(arr, idx):
#     answer = 0
#     arr = arr[idx:]
#     for i in range(len(arr)):
#         if arr[i] == 1:
#             answer = i+idx
#         elif arr[i] == 0:
#             continue
#         elif arr[i] != 0 and arr[i] != 1:
#             answer = -1
            
#     return answer

def solution(arr, idx):
    # idx보다 큰 위치부터 배열 끝까지 확인
    for i in range(idx , len(arr)):
        if arr[i] == 1:
            return i  # 첫 번째 1 발견 시 바로 반환
    return -1  # 1이 없으면 -1 반환


arr = [0, 0, 0, 1]
idx = 1
print(solution(arr, idx))

# range()를 응용해서 사용하기 , idx뒷부분만 필요하기에 조건을 뒷부분만 보고 판단하기