def solution(array):
    count = {}
    for num in array:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    #  빈 딕셔너리 count 만들고 그 안에 쌍 지어주기
    max_mode = max(count.values())
    # max값 구하기
    mode = []
    for key in count:
        if count[key] == max_mode:
            mode.append(key)
    # count에서 key값을 따로 때어주고 최빈값과 같으면 mode 리스트에 추가
    if len(mode) > 1:
        return -1
    else:
        return mode[0]
    # 최빈값이 두개 이상이면 -1 출력 아니면 최빈값 출력


array = [1, 2, 3, 3, 3, 4]
print(solution(array))

# 딕셔너리에서 value랑 key 좀더 잘 활용하기