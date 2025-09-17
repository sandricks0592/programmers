def solution(arr, delete_list):
    answer = []
    for d in range(len(delete_list)):
        if delete_list[d] == arr:
            arr.remove(delete_list[d])
    arr = answer
    return answer

arr = [293, 1000, 395, 678, 94]	
delete_list = [94, 777, 104, 1000, 1, 12]
print(solution(arr, delete_list))