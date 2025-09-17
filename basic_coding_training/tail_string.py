def solution(str_list, ex):
    answer = ''
    for sl in str_list:
        if ex not in sl:
            answer += sl
    return answer

str_list = ["abc", "def", "ghi"]
ex = 'ef'
print(solution(str_list, ex))