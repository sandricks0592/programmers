def solution(myString):
    answer = ''
    myString = list(myString)
    for i in range(len(myString)):
        if myString[i] == 'a' or myString[i] == "A":
            answer += 'A'
        else:
            answer += myString[i].lower()
    return "".join(answer)

myString = "abstract algebra"
print(solution(myString))