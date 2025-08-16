# 직각삼각형의 한 변 길이 : int a
# 빗변 길이 : int c
# 다른 한 변의 길이의 제곱 : int b_square
a = int( input())
c = int( input())

def pythagoras (a,c):
    if a <= 0 or c <= 0:
        return 0
    else :
        b_square = c ** 2 - a ** 2 
        return b_square


print(pythagoras(a,c))