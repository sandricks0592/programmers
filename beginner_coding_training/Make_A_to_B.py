# def solution(before, after):
#     str_before = str(before)
#     str_after = str(after)
#     if str_before[::-1] == str_after:
#         answer =1
#     else:
#         answer = 0
#     return answer

def solution(before, after):
    str_before = str(before)
    str_after = str(after)
    if sorted(str_before) == sorted(str_after):
        answer =1
    else:
        answer = 0
    return answer

before = 'pplea'
after = 'apple'
print(solution(before, after))

# 문자를 섞는다는거지 무조건 앞뒤를 바꾼다는 생각에 갇히지말기