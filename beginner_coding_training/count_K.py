def solution(i, j, k):
    answer = 0
    str_k = str(k)
    for a in range(i,j+1):
        if str_k in str(a): 
            answer += str(a).count(str_k)
    return answer

i = 1
j = 13
k = 1
print(solution(i, j, k))

# .count 이용하기!!