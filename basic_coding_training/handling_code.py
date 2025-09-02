# def solution(code):
#     answer = ''
#     ret = ''
#     mode = 0
#     for i in range(len(code)):
#         if code[i] == 1:
#             if mode == 0:
#                 mode = 1
#         if mode == 0:
#             if code[i] != 1 and i%2 == 0:
#                 answer += ret + code[i]
#             elif code[i] == 1:
#                 mode = 1
#         elif mode == 1:
#             if code[i] != 1 and i %2 == 1:
#                 answer += ret + code[i]
#             elif code[i] == 1:
#                 mode = 1 
#     return 


def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if code[i] == "1":  # 문자열 비교
            mode = 1 - mode  # 토글
        else:
            if mode == 0 and i % 2 == 0:
                answer += code[i]
            elif mode == 1 and i % 2 == 1:
                answer += code[i]
    return answer if answer else "EMPTY"

print(solution("abc1abc1abc"))
