def solution(my_string, m, c):
    answer = ''
    my_string = list(my_string)
    answer = my_string[c-1::m]
    answer = ''.join(answer)
    return answer

my_string = "ihrhbakrfpndopljhygc"
m = 4
c = 2
print(solution(my_string, m, c))