def solution(myString):
    answer = []
    A = myString.split('x')
    for i in A:
        A = len(i)
        answer.append(A)
    return answer

myString = "oxooxoxxox"
print(solution(myString))