# 직사각형을 만드는데 필요한 4개의 점 중 3개의 좌표가 주어질 때, 나머지 한 점의 좌표를 구하려고한다. 
# 점 3개의 좌표가 들어있는 배열v가 매개변수로 주어질 때, 
# 직사각형을 만드는데 필요한 나머지 한점의 좌표를 return 하도록 solution함수를 완성하시오

def solution(v):
    x_list = [x for x, y in v]  # 리스트로 생성해야 함
    y_list = [y for x, y in v]
    
    for x in x_list:
        if x_list.count(x) == 1:
            x_result = x
            
    for y in y_list:
        if y_list.count(y) == 1:
            y_result = y
            
    return [x_result, y_result]

print(solution([[1, 4], [3, 4], [3, 10]]))  # [1, 10]
