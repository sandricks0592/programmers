def solution(num_list):
    answer = 0
    for i in range(len(num_list)):
        if all(v>0 for v in num_list):
            answer = -1
        elif num_list[i] < 0:
            answer = i
            return answer
    return answer

num_list = [12, 4, 15, 46, 38, -2, 15]
print(solution(num_list))

# 전체 조건이 달릴 때는 all사용하기, 첫번째 음수만 출력하는 조건을 만족시키기 위해 출력하고 바로 종료(return)