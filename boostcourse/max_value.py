# int list : numbers

def max_value(numbers):
    answer = 0
    numbers.sort()
    answer = numbers[-2]*numbers[-1]
    return answer


print(max_value(numbers = [ 1,2,3,4,5,6]))
    