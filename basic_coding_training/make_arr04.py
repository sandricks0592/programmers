def solution(arr):
    stk = []
    i = 0 
    
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()
    return stk
arr = [1,4,2,5,3]
print(solution(arr))

# 정확한 범위를 모를때는 while을 사용하자. 마지막 원소를 삭제할 떄는 pop을 사용한다.