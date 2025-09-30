def solution(num_list):
    answer = []
    answer= sorted(num_list,reverse=True)
    return sorted(answer[-5:])

num_list = [12, 4, 15, 46, 38, 1, 14]
print(solution(num_list))