def solution(array):
    array = sorted(array)
    answer = array[len(array)//2]
    return answer

array = [1, 2, 7, 10, 11]	
print(solution(array))