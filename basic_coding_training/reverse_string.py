# def solution(my_string, s, e):
#     answer = ''
#     my_string= list(my_string)
#     new_str = my_string[e+1:s:-1]
#     answer = my_string[0:s]+new_str+my_string[e+1:]
#     return answer

def solution(my_string, s, e):
    answer = ''
    my_string = list(my_string)
    my_string[s:e+1] = my_string[s:e+1][::-1]
    answer = "".join(my_string)
    return answer

my_string = "Progra21Sremm3"
s = 6
e = 12

print(solution(my_string, s, e))

# join 기억하기, 순서 바꾸는거 기억하기