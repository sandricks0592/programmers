# def solution(picture, k):
#     answer = []
#     for i in picture:
#         for j in range(len(i)):
#             answer.append(str(i[j])*k)
#     return answer

def solution(picture,k):
    answer = []
    for row in picture:
        new_row = ''
        for ch in row:
            new_row += ch * k
            for _ in range(k):
                answer.append(new_row)

    return answer

picture = [".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."]
k = 2
print(solution(picture, k))