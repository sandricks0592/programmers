# def solution(my_string, indices):
#     answer = ''
#     my_string = list(my_string)
#     for i in indices:
#         answer = my_string[:i]+my_string[i+1:]
        
#     return answer

def solution(my_string, indices):
    my_string = list(my_string)  # 리스트로 변환
    
    for i in sorted(indices, reverse=True):  # 뒤에서부터 삭제
        del my_string[i]  # 해당 인덱스 삭제
        
    return ''.join(my_string)


my_string = "apporoograpemmemprs"
indices = [1, 16, 6, 15, 0, 10, 11, 3]	
print(solution(my_string, indices))

#  my_string을 변화시키기 위해 sorted를 사용하고, 값이 밀리는걸 방지하기 위해 내림차순을 해준다.