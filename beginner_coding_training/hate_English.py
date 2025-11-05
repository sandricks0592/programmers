def solution(numbers):
    a = {
       "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9",
        "ten":"10"
    }
    for num,digit in a.items():
        numbers = numbers.replace(num,digit)
    return numbers

numbers = "onetwothreefourfivesixseveneightnine"
print(solution(numbers))

