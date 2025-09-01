# def solution(my_string, alp):
#     answer = ''
#     for i in range(len(my_string)):
#         if my_string[i] == alp[0]:
#             answer = my_string[:i]+my_string[i].upper()+my_string[i+1:]    
#         else:
#             answer = my_string       
#     return answer
#  위 코드는 하나만 대문자로 만들수 있다. 중복일 경우 불가능

def solution(my_string, alp):
    answer = ''
    answer = my_string.replace(alp,alp.upper())
    return answer


print(solution("programmers","p"))

# replace 사용법 기억하기