def solution(arr):
    answer = []
    i = 0
    answer = []
    while i < len(arr):
        if len(answer) == 0:
            answer.append(arr[i])
            i += 1
        elif len(answer) > 0 and answer[-1] == arr[i]:
            answer.pop(-1)
            i += 1
        elif len(answer) > 0 and answer[-1] != arr[i]:
            answer.append(arr[i])
            i += 1
    if len(answer) > 0:
        return answer
    else:
        return [-1]
    

arr = [0, 1, 1,0]
print(solution(arr))