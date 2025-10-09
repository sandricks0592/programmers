def solution(slice, n):
    count = 0
    piece = slice
    if n % piece == 0:
        return n // piece
    else:
        while piece < n:
            piece += slice
            count += 1
        return count+1
    

slice = 4
n = 12
print(solution(slice, n))