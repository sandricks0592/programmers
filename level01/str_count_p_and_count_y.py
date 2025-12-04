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

# 카운트 갯수가 서로 같으면 1을 출력하고 다르면 0을 출력한다.