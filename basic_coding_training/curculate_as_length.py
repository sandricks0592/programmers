# def solution(num_list):
#     answer = 0
#     if len(num_list) >= 11:
#         for i in num_list:
#             answer += i
#     elif len(num_list) <= 10:
#         for i in num_list:
#             answer *= i
#     return answer

def solution(num_list):
    if len(num_list) >= 11:
        answer = 0
        for i in num_list:
            answer += i
    elif 0 < len(num_list) <= 10:
        answer = 1
        for i in num_list:
            answer *= i
    return answer

num_list = [2, 3, 4, 5]
print(solution(num_list))

#  answer 초기 값을 생각하기