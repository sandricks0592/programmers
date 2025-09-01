def solution(str1, str2):
    answer = ''
    min_len = min(len(str1), len(str2))

    # 번갈아 붙이기 (짧은 길이 기준)
    for i in range(min_len):
        answer += str1[i] + str2[i]

    # 남은 문자열 붙이기
    if len(str1) > min_len:
        answer += str1[min_len:]
    if len(str2) > min_len:
        answer += str2[min_len:]

    return answer
    

str1 = "aaaaa"
str2 = "bbbbbbb"

print(solution(str1,str2))

# min을 이용하여 문제를 해결하는 방법을 기억하고 남은 문자열 붙이는 디테일을 좀더 유의하기!
