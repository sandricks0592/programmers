def solution(my_string, queries):
    answer = ''
    my_string = list(my_string)
    for s,e in queries:
        my_string[s:e+1] = my_string[s:e+1][::-1]

        answer = ''.join(my_string)
    return answer

my_string = "rermgorpsam"
queries = [[2, 3], [0, 7], [5, 9], [6, 10]]

print(solution(my_string, queries))