# def solution(n):
#     factorial = 1
#     count = 0
#     i = 0
#     if n<4:
#         return 0
#     else:
#         while factorial< n:
#             i += 1
#             count += 1
#             factorial *= (i+1)
#         answer = count
#     return answer

def solution(n):
    factorial = 1
    i = 1
    
    while factorial * (i + 1) <= n:
        i += 1
        factorial *= i

    return i

n = 7
print(solution(n))

# *=는 하나씩 곱하는거 잊지말기