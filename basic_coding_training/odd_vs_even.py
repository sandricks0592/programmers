def solution(num_list):
    answer = 0
    odd_total = 0
    even_total = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            even_total +=  num_list[i]
        elif i % 2 == 1:
            odd_total += num_list[i]
    if even_total > odd_total:
        answer = even_total
    elif odd_total > even_total:
        answer = odd_total
    else:
        answer = odd_total
    return answer

num_list = [4, 2, 6, 1, 7, 6]
print(solution(num_list))