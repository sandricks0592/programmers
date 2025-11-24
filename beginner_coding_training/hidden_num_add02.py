# def solution(my_string):
#     answer = 0
#     ch_num = ''
#     for i in my_string:
#         if i.isdigit():
#             answer += int(i)
#         else:
            
#     return answer

# my_string = "aAb1B2cC34oOp"
# print(solution(my_string))

def solution(my_string):
    for c in my_string:
        if not c.isdigit():   # 숫자가 아니면
            my_string = my_string.replace(c, ' ')
    nums = my_string.split()
    
    return sum(map(int, nums)) if nums else 0

my_string = "aAb1B2cC34oOp"	
print(solution(my_string))

# 문자들은 공백으로 replace한 다음 split하여 숫자들을 빼준다음 int형으로 만들어 다 더해준다ㅑ.