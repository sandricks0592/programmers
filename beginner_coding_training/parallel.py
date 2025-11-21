#     # dots로 만들수 있는 lines 배열
# def get_lines(dots):
#     lines = []
#     n = len(dots)
#     for i in range(n):
#         for j in range(i+1,n):
#             lines.append((dots[i],dots[j]))
#     return lines
# def solution(dots):
#     lines = get_lines(dots)

#     slopes = []
#     for(x1,y1),(x2,y2) in lines:
#         slope = (y2-y1) / (x2-x1)
#         slopes.append(slope)

#         for i in range(len(slopes)):
#             for j in range(i+1, len(slopes)):
#                 if slopes[i] == slopes[j]:
#                     answer = 1
#     return 0

def solution(dots):
    A, B, C, D = dots

    def slope(p1, p2):
        return (p2[1]-p1[1]) / (p2[0]-p1[0])

    # 세 가지 선분 쌍 비교
    if slope(A,B) == slope(C,D):
        return 1
    if slope(A,C) == slope(B,D):
        return 1
    if slope(A,D) == slope(B,C):
        return 1
    return 0


dots = [[1, 4], [9, 2], [3, 8], [11, 6]]
print(solution(dots))

# 기울기는 x 값의 차 분의 y값의 차를 생각하기