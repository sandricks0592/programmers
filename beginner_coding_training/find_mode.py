def solution(array):
    count = {}
    for num in array:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    #  빈 딕셔너리 count 만들고 그 안에 쌍 지어주기
    max_mode = max(count.values())
    answer = max_mode
    return answer

array = [1, 2, 3, 3, 3, 4]
print(solution(array))