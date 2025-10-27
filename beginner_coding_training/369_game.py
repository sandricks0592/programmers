def solution(order):
    str_order = str(order)
    answer = 0
    for ch in str_order:
        if ch in ['3','6','9']:
            answer += 1
    return answer

order = 3478590
print(solution(order))

#  