# def solution(strArr):
#     answer = []
#     for i in strArr:
#         if  in i:
#             strArr.remove(i)
#         else:
#             strArr.append(i)    
#     return answer

def solution(strArr):
    answer = []
    for s in strArr:        # strArr의 원소를 하나씩 확인
        if "ad" not in s:   # 문자열에 "ad"가 포함되지 않았다면
            answer.append(s)  # 결과 리스트에 추가
    return answer


strArr = ["and","notad","abcd"]
print(solution(strArr))

