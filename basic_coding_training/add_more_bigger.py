# a,b = map(int,input().split(" "))
# def solution():
#     answer = 0
#     ab = str(a)+str(b)
#     ba = str(b)+str(a)
#     if int(ab) > int(ba):
#         answer = ab
#     elif int(ba) > int(ab):
#         answer = ba
#     else:
#         answer = ab
    
#     return int(answer)

a,b = map(int,input().split(" "))
def solution():
    answer = 0
    ab = str(a)+str(b)
    ba = str(b)+str(a)
    if int(ab >= ba):
        answer = ab
    else:
        answer = ba
    
    return int(answer)


print(solution())

# 조건문에서 겹치는부분은 유동적으로 잘 생각해보기