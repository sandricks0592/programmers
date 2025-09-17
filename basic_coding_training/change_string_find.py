def solution(myString, pat):
    answer = 0
    change_myString = []
    for i in range(len(myString)):
        if myString[i] == 'A':
            change_myString += 'B'
        else:
            change_myString += 'A'
    
    if pat in change_myString:
        answer = 1
    return answer

myString = "ABBAA"
pat = "AABB"
print(solution(myString, pat))