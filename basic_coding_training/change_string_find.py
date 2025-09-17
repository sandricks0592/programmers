# def solution(myString, pat):
#     answer = 0
#     change_myString = ''
#     for i in range(len(myString)):
#         if myString[i] == 'A':
#             change_myString += 'B'
#         else:
#             change_myString += 'A'
    
#     if pat in change_myString:
#         answer = 1
#     return answer

def solution(myString, pat):
    # 1. A ↔ B 치환
    swapped = ""
    for ch in myString:
        if ch == "A":
            swapped += "B"
        else:  # ch == "B"
            swapped += "A"

    # 2. 부분 문자열 확인
    if pat in swapped:
        return 1
    else:
        return 0


myString = "ABBAA"
pat = "AABB"
print(solution(myString, pat))