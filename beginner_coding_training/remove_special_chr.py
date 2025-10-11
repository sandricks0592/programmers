def solution(my_string, letter):
    answer = ''
    for ch in my_string:
        if ch != letter:
            answer += ch
    return answer

my_string = "abcdef"
letter = 'f'
print(solution(my_string, letter))

# string도 쪼개어서 비교 사용 가능하다.