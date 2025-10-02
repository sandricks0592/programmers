# def solution(picture, k):
#     answer = []
#     for i in picture:
#         for j in range(len(i)):
#             answer.append(str(i[j])*k)
#     return answer

def solution(picture, k):
    answer = []

    for row in picture:
        new_row = ""              # 한 행 전체를 담을 변수
        for ch in row:            # row 안의 문자 하나씩
            new_row += ch * k     # 문자 수평 확대

        for _ in range(k):        # 수직 확대
            answer.append(new_row)

    return answer


# def solution(picture, k):
#     answer = []
#     for i in range(len(picture)):
#         for _ in range(k):
#             answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))
#     return answer

picture = [".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."]
k = 2
print(solution(picture, k))

# for 문 여러개로 string을 분리 가능하다. 가로 세로 잘 구별해서 사용하기, replace도 사용 가능하다.