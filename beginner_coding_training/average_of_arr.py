def solution(numbers):
    answer = 0
    sum = 0
    for i in numbers:
        sum += i
    answer = sum / len(numbers)
    return answer

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(solution(numbers))