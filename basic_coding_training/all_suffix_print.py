def solution(my_string):
    answer = []
    a = []
    for i in range(len(my_string)):
        a.append(my_string[i:])
        answer = sorted(a)
    return answer

print(solution("banana"))