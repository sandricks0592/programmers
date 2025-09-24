# def solution(myStr):
#     answer = []
#     if any(ch in myStr for ch in ["a","b","c"]):
#         A = myStr.replace("a","c").replace("b","c").split("c")
#         if all(i == "c" for i in A) :
#             answer = ["EMPTY"]
#         else:
#             for i in A:
#                 if i != '':
#                     answer.append(i)
#     return answer

def solution(myStr):
    answer = []
    # "a"와 "b"를 "c"로 바꾸고 "c" 기준으로 split
    A = myStr.replace("a", "c").replace("b", "c").split("c")

    # 빈 문자열 제거
    for i in A:
        if i != '':
            answer.append(i)

    # 다 지워져서 아무것도 안 남으면 ["EMPTY"]
    if not answer:
        answer = ["EMPTY"]

    return answer

myStr = "dddddd"
print(solution(myStr))