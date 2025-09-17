# def solution(arr, delete_list):
#     answer = []
#     for d in range(len(delete_list)):
#         if delete_list[d] == arr:
#             arr.remove(delete_list[d])
#     arr = answer
#     return answer

def solution(arr, delete_list):
    answer = []
    for num in arr:               # arr의 원소를 하나씩 보면서
        if num not in delete_list:  # delete_list에 없으면
            answer.append(num)      # 결과에 추가
    return answer


arr = [293, 1000, 395, 678, 94]	
delete_list = [94, 777, 104, 1000, 1, 12]
print(solution(arr, delete_list))

# not in 사용해보기