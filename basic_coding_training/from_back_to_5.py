def solution(num_list):
    answer = []
    answer= sorted(num_list,reverse=True)
    return sorted(answer[-5:])

num_list = [12, 4, 15, 46, 38, 1, 14]
print(solution(num_list))

# sorted(,reverse=True)를 잘 활용하기, 음수 슬라이스할떄는 범위 잘 생각하기