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