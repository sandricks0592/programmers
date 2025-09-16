# def solution(my_string):
#     answer = []
#     my_string = list(map(str.upper, my_string))
#     for i in my_string:
#         if i == 'A':
#             answer += 1
#         elif i !=
#         .
#         .
#         .
#         .
    
#     return answer

def solution(my_string):
    answer = []
    answer = [0]*52 # 미리 리스트를 만들기
    for c in my_string:
        if'A' <= c <= 'Z':
            answer[ord(c)-ord('A')] += 1    # 대문자
        elif'a' <= c <= "z":
            answer[ord(c)-ord('a')+26] += 1    # 소문자

    return answer
my_string = "Programmers"
print(solution(my_string))

# ord()는 아스키 코드를 이용, 아스키 코드의 차로 인덱스 구별, 아스키 코드 번호를 확인해보고 차별성을 두기 위해 26 더하는 것 까지 기억하기