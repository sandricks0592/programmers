def solution(num_list, n):
    answer = []
    answer = num_list[::n]
    return answer

num_list = [4, 2, 6, 1, 7, 6]
n = 2
print(solution(num_list, n))