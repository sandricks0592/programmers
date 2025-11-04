def solution(my_str, n):
    answer = []
    for i in range(0,len(my_str),n):
        answer.append(my_str[i:i+n])
    return answer

my_str = "abc1Addfggg4556b"
n = 6
print(solution(my_str, n))

#  range()를 안쓰고 str[]를 할 경우 문자 하나씩 불러와 원하는 결과를 못 얻는다.