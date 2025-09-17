def solution(arr):
    answer = []
    number_two = []
    for i in range(len(arr)):
        if arr[i] == 2:
            number_two.append(i)
        else:
            answer = number_two    
    if len(number_two) > 0:
        answer = arr[number_two[0]:number_two[-1]+1]
    else:
        answer = [-1]
    return answer

arr = [1, 2, 1, 4, 5, 2, 9]
print(solution(arr))