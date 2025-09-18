def solution(n_str):
    answer = ''
    n_str = list(n_str)
    for i in range(len(n_str)):
        if n_str[i]!= '0':
            answer = n_str[i:]
            return ''.join(answer)
    

n_str = '0010'
print(solution(n_str))

# ''.join은 리스트를 문자열로 다시 바꿔주는거 기억하기