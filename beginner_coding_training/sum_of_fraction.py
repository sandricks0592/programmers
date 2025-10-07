from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    A = Fraction(numer1, denom1 )  
    B = Fraction(numer2, denom2)
    sum = A + B
    numerator = sum.numerator
    denominator = sum.denominator
    answer = [numerator,denominator]
    return answer

numer1 = 1
denom1 = 2
numer2 = 3
denom2 = 4
print(solution(numer1, denom1, numer2, denom2))