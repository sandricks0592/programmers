def solution(polynomial):
    answer = ''
    temp = polynomial.split(" + ")
    x_sum = 0
    num_sum = 0

    for i in temp:
        if 'x' in i:
            if i == 'x':
                x_sum += 1
            else:
                x_sum += int(i.replace('x',''))
        else:
            num_sum += int(i)

    if x_sum == 1 and num_sum != 0:
        answer = f"x + {num_sum}"
    elif x_sum == 1 and num_sum == 0:
        answer = 'x'
    elif x_sum != 0 and num_sum != 0:
        answer = f"{x_sum}x + {num_sum}"
    elif x_sum != 0 and num_sum == 0:
        answer = f"{x_sum}x"
    elif x_sum == 0 and num_sum != 0:
        answer = f"{num_sum}"
    elif x_sum == 0 and num_sum == 0:
        answer = ''

    return answer

polynomial = "3x + 7 + x"	
print(solution(polynomial))

# x를 replace로 없애주는 방법도 있다.