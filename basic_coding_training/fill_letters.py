def solution(my_string, indices):
    answer = ''
    my_string = list(my_string)
    while i in indices:
        answer = my_string[:i]+my_string[i+1:]
        
    return answer

my_string = "apporoograpemmemprs"
indices = [1, 16, 6, 15, 0, 10, 11, 3]	
print(solution(my_string, indices))