def solution(my_string):
    answer = ''
    for ch in my_string:
        if ch not in answer:
            answer += ch
    return answer

my_string = 'people'
print(solution(my_string))

#  빈 문자열을 이용하면 더욱 쉽게 구할수 있다.