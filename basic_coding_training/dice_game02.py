# a,b,c = map(int, input().split(" "))
# def solution(a, b, c):
#     answer = 0
#     if a > 0 and b > 0 and c > 0:
#         if a <=6 and b <= 6 and c <= 6:
#             if a != b and b != c and c != a:
#                 answer = a + b + c
#             elif a == b != c or b == c != a or c == a != b:
#                 answer = (a+b+c)*(a**2+b**2+c**2)
#             elif a == b == c:
#                 answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
#         else:
#             return 0
#     else:
#         return 0
#     return answer

# print(solution(a,b,c))

def solution(a, b, c):
    # 세 숫자가 모두 같을 때
    if a == b == c:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    # 세 숫자 중 두 개만 같을 때
    elif a == b or b == c or a == c:
        return (a + b + c) * (a**2 + b**2 + c**2)
    # 세 숫자가 모두 다를 때
    else:
        return a + b + c

# 조건을 좀 더 디테일하게 생각하기