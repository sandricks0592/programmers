def solution(n, k):
    answer = []
    if n >=1 :
        answer = list(range(k,n+1,k))
    else:
        return answer
    return answer

print(solution(6,3))