def solution(myString):
    answer = []
    A = myString.split('x')
    for i in A:
        if i != '':
            answer.append(i)
    answer.sort()
    return answer

myString = "axbxcxdx"
print(solution(myString))

# ''같은 요소는 삭제하는거 기억하고 .sort()는 리스트 자체는 정렬하지만 None을 반환하기에 따로 return 해줘야 한다.