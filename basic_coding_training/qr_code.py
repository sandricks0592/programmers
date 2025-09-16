def solution(q, r, code):
    answer = ''
    code = list(code)
    answer = code[r::q]    
    return ''.join(answer)

q = 3
r = 1
code = 	"qjnwezgrpirldywt"	
print(solution(q, r, code))