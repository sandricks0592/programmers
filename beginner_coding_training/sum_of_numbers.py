def solution(num, total):
    answer = []
    x = (total - num*(num - 1)/2)/num
    for i in range(num):
        answer.append(int(x + i))
    return answer

num = 3
total = 12
print(solution(num, total))