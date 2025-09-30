# def solution(strArr):
#     answer = 0
#     num = []
#     for i in range(len(strArr)):
#         if len(strArr[i]) != 0:
#             num.append(len(strArr[i]))
#     answer = max(num, key =num.count)
    
#     return num.count(answer)

def solution(strArr):
    answer = 0
    length_count = {}
    for i in strArr:
        l = len(i)
        length_count[l] = length_count.get(l, 0) +1
    answer = max(length_count.values())
    return answer

strArr = ["a","bc","d","efg","hi"]
print(solution(strArr))

# dic사용하는 방법과 .get()메서드 사용하는 방법 생각하기