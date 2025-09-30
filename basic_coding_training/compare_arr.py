def solution(arr1, arr2):
    answer = 0
    A,B = 0,0
    for a in range(len(arr1)):
        A += arr1[a]
    for b in range(len(arr2)):
        B += arr2[b]
    if len(arr1) == len(arr2):
       
        if A == B:
            answer = 0
        elif A > B:
            answer = 1
        else:
            answer = -1
    elif len(arr1) > len(arr2):
        answer = 1
    else:
        answer = -1
        
    return answer

arr1 = [49, 13]
arr2 = [100, 17, 84, 1]
print(solution(arr1, arr2))