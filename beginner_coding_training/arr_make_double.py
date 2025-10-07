def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(2*i)
    return answer

numbers = [1,2,3,4,5]
print(solution(numbers))