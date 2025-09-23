def solution(myString, pat):
    answer = ''
    myString = list(myString)
    pat = list(pat)
    for i in range(len(myString)):
        if pat[-1] == myString[i]:
            answer = myString[:i+1]
    return ''.join(answer)

myString = "AbCdEFG"
pat = "dE"
print(solution(myString, pat))