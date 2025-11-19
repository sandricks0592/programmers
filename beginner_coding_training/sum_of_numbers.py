def solution(num, total):
    answer = []
    x = (total - num*(num - 1)/2)/num
    for i in range(num):
        answer.append(int(x + i))
    return answer

num = 3
total = 12
print(solution(num, total))

# x + (x+1) + (x+2) + ... + (x + num -1) 이 값을
# num * x + ( 0 + 1 + ... + num-1) 으로 바꿔준다.
# num * x + num * (num-1)/2 = total이 된다.
# 이걸 응용해 시작값을 구해서 계산한다.
