def solution(num_list):
    answer = 0
    add = 0
    mul = 0
    for i in range(len(num_list)):
        add += num_list[i]
        mul *= num_list[i]
        if add**2 > mul:
            answer = 1
        elif mul > add**2:
            answer = 0
    return answer

# 곱은 초기 변수 선언에서 0으로 하면 무슨 수를 곱하든 0이다.