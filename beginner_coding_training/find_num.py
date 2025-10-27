# def solution(num, k):
#     answer = 0
#     if k in str(num):
#         answer += 1
#     elif k not in str(num):
#         answer = -1
#     return answer

def solution(num,k):
    num_str = str(num)
    k_str = str(k)

    if k_str in num_str:
        answer = num_str.index(k_str)+1
    else:
        answer = -1
    return answer

num = 29183
k = 1
print(solution(num, k))


# str으로 비교할때 두개 다 바꾸는거 기억하기.