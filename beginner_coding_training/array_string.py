def solution(my_string):
    answer = ''
    lst = list(my_string.lower())
    lst.sort()
    answer = ''.join(lst)
    return answer

my_string = "Bcad"
print(solution(my_string))

#  sort는 list에만 가능하다. 분리해서 사용하기!!