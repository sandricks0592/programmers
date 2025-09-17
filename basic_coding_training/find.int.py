def solution(num_list, n):
    answer = 0
    for i in range(len(num_list)):
        if num_list[i] == n:
            answer = 1
            
    return answer

num_list = [1,2,3,4,5]
n = 3
print(solution(num_list, n))