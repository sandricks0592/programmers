# def solution(intStrs, k, s, l):
#     answer = []
#     for i in range(len(intStrs)):
#         if int(intStrs[i][s:s+l]) > k:
#             answer.append(int(intStrs[i][s:s+l+1]))
#         else:
#             answer
#     return answer


def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        part = int(num[s:s+l])
        if part>k:
            answer.append(part)
    return answer


intStrs = ["0123456789","9876543210","9999999999999"]
k = 50000
s = 5
l = 5

print(solution(intStrs, k, s, l))