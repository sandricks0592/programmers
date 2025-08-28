# def solution(my_strings, parts):
#     answer = []
#     for s, idx in zip(my_strings,parts):
#         start, end = idx
#         answer.append(s[start: end+1])
#     return answer
#  오답 / 문제를 잘못 해석. list 두개를 엮어야할땐 zip 사용

def solution(my_strings, parts):
    answer = ''
    a = []
    for s,idx in zip(my_strings,parts):
        start, end = idx
        a.append(s[start:end+1])
    answer = ''.join(a)
    return answer

my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"]
parts = [[0, 4], [1, 2], [3, 5], [7, 7]]
print(solution(my_strings,parts))

