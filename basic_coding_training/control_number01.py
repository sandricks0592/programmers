def solution(n, control):
    answer = 0
    answer = n
    for i in range(len(control)):
        if control[i] == 'w':
            answer += 1
        elif control[i] == 's':
            answer += -1
        elif control[i] == 'd':
            answer += 10
        elif control[i] == 'a':   
            answer += -10
    return answer

control = "wsdawsdassw"	
n = 0
print(solution(n,control))