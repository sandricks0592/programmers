# def solution(s):
#     S = s.lower()
#     p = S.count('p')
#     y = S.count('y')
#     if p == 0 or y == 0:
#         answer = True
#     elif p == y:
#         answer = True
#     else:
#         answer = False
#     return answer

def solution(s):
    S = s.lower()
    return S.count('p') == S.count('y')

s = 'PpoooyY'
print(solution(s))