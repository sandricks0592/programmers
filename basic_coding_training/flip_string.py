def solution(my_string, queries):
    answer = ''
    my_string = list(my_string)
    for s,e in queries:
        my_string[s:e+1] = my_string[s:e+1][::-1] # 이부분

        answer = ''.join(my_string)
    return answer

my_string = "rermgorpsam"
queries = [[2, 3], [0, 7], [5, 9], [6, 10]]

print(solution(my_string, queries))

# 문자열 뒤집는 슬라이스 잘 기억하기 start와 stop의 크기에 따라 표기 방법이 달라진다.