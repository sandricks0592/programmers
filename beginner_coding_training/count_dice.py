def solution(box, n):
    answer = (box[0] // n) * (box[1] // n) * (box[2] // n)
    return answer

box = [10,8,6]
n = 3
print(solution(box, n))

#  간단하게 생각하기