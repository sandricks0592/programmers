def solution(numbers, num1, num2):
    answer = []
    answer = numbers[num1:num2+1]
    return answer

numbers = [1, 2, 3, 4, 5]
num1 = 1
num2 = 3
print(solution(numbers, num1, num2))