def solution(str_list):
    answer = []
    for i in range(len(str_list)):
        if str_list[i] == "l":
            answer = str_list[:i]
            return answer
        elif str_list[i] == "r":
            answer = str_list[i+1:]
            return answer

    return answer

str_list = ["r","r","d","r"]	
print(solution(str_list))

#  if 조건문의 위치에 따라 바로 끝나버릴수도있기에 l, r 둘다 아닐 경우는 따로 빼준다는걸 기억하기