# def solution(my_string):
#     answer = ''
#     my_string = list(my_string)
#     for i in my_string:
#         if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#             my_string.pop(i)
#     answer = mu_string
#     return answer

def solution(my_string):
    answer = ''
    vowel = 'aeiou'

    for ch in my_string:
        if ch not in vowel:
            answer += ch
    return answer

my_string = 'bus'
print(solution(my_string))