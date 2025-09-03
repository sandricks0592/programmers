# def solution(a, d, included):
#     answer = 0
#     b = []
#     for i in range(len(included)):
#         b += a+i*d
#     for e in zip(b, included):
#         answer = e
#     return answer

def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        term = a + d * i   # i번째 항 (등차수열: a₁ + (i)*d)
        if included[i]:    # included[i]가 True일 때만 더함
            answer += term
    return answer

print(solution(3,4,	[True,False,False,True,True]))