# def solution(l, r):
#     answer = []
#     for i in range(l,r+1):
#         if i / 10 == 5:
#             answer.append(i)
#     return answer

def solution(l,r):
    answer = []
    for a in range(l,r+1):
        str_a = str(a)
        is_valid = True
    
        for i in range(len(str_a)):
            if str_a[i] != '0' and str_a[i] != '5':
                is_valid = False
                break
        if is_valid:
            answer.append(a)
    if len(answer) == 0:
        answer = [-1]
    else:
        answer = answer
    return answer

print(solution(5,555))
print(solution(10,20))

# is_valid를 사용하여 불리언을 이용하는걸 익숙해지자.