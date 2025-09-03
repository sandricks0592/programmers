# def solution(num_list):
#     answer = 0
#     odd = ''
#     even = ''
#     for i in range(0,len(num_list),2):
#         even += str(num_list[i])
#     for e in range(1,len(num_list),2):
#         odd += str(num_list[e]) 
#     answer = int(odd) + int(even)
#     return answer


def solution(num_list):
    answer = 0
    odd = ''
    even = ''
    for i in range(len(num_list)):
        if num_list[i]%2 ==0:
            even += str(num_list[i])
        elif num_list[i]%2 ==1:
            odd += str(num_list[i])
    answer = int(odd) + int(even)
    return answer


num_list = [3,4,5,2,1]

print(solution(num_list))

# 문제 조금더 자세히 보기! 문자열 + int 할 때 오류 발생 주의하기!