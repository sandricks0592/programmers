def solution(age):
    answer = ''
    for i in str(age):
        answer += chr(ord('a')+int(i))
    return answer

age = 23
print(solution(age))

# int를 str로 만들어 분리 한 후 ord()를 사용한다.