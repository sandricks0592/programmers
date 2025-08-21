def solution(num_list, n):
    answer = []
    front = num_list[:n]
    back = num_list[n:]
    answer = back+front
    return answer

# 기존 배열을 슬라이싱해준다음 새로운 배열에 저장하고 더해준다.