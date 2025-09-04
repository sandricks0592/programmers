# def solution(myString):
#     answer = ''
#     for i in range(len(myString)):
#         if myString.upper()[i] <= 'I':
#             answer = myString[:i]+'I'+myString[i+1:]
#     return answer

def solution(myString):
    answer = ''
    for ch in myString:
        if ch.upper() <= "L":
            answer += "l"
        else:
            answer += ch
    return answer

myString = "abcdevwxyz"
print(solution(myString))