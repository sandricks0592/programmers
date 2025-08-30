def solution(my_string, overwrite_string, s):
    answer = ''
    answer = my_string[:s]+overwrite_string+my_string[s+len(overwrite_string):]
    return answer

# 뒤 my_string삽입 조건을 좀 더 생각해보기