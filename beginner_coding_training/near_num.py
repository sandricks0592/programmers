def solution(array, n):
    return min(array, key = lambda x : (abs(x-n),x))
    
array = [3, 10, 28]
print(solution(array, n))

# lambda를 이용해보기!!!