def solution(num_list):
    answer = 0
    x = 0
    for i in range(len(num_list)):
        while int(num_list[i]) >= 1:
            if int(num_list[i]) % 2 == 0:
                num_list[i]) = int(num_list[i]) // 2
                x += 1
            elif int(num_list[i]) % 2 == 1:
                int(num_list[i]) = (int(num_list[i]) - 1) // 2
                x += 1
        answer = x
    return answer

num_list = [12, 4, 15, 1, 14]
print(solution(num_list))

# 연산에서 합차가 먼저인지 곱 나누기가 먼저인지 생각해보기
# range()를 이용하면 시간이 오버 할 수 있어서 바로 num_list 요소를 사용할 수 있게 해보자.