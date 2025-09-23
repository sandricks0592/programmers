def solution(binomial):
    answer = 0
    A = binomial.split(" ")
    if A[1] == '+':
        answer = int(A[0]) + int(A[2])
    elif A[1] == '-':
        answer = int(A[0]) + int(A[2])
    elif A[1] == '*':
        answer = int(A[0]) * int(A[2])
    return answer

binomial = "43 + 12"
print(solution(binomial))