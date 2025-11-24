# def solution(babbling):
#     answer = 0
#     pnc = ['aya', 'ye', 'woo', 'ma']
#     for i in babbling:
#         for e in pnc:
#             if e in i:
#                 answer += 1
#     return answer

def solution(babbling):
    answer = 0
    words = ['aya', 'ye', 'woo', 'ma']

    for b in babbling:
        temp = b
        for w in words:
            temp = temp.replace(w,' ')

        temp = temp.replace(' ','')

        if temp == '':
            answer += 1


    return answer

babbling = ["aya", "yee", "u", "maa", "wyeoo"]
print(solution(babbling))