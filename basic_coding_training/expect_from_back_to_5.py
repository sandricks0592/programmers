def solution(num_list):
    answer = []
    num_list = sorted(num_list,reverse = True)
    answer = num_list[:-5]
    return sorted(answer)

num_list = [12, 4, 15, 46, 38, 1, 14, 56, 32, 10]
print(solution(num_list))