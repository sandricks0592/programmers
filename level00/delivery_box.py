def solution(n, w, num):
    # 1. 창고 배열 만들기
    warehouse = []  # 2차원 리스트
    box_num = 1
    while box_num <= n:
        layer = [0] * w
        for i in range(w):
            if box_num > n:
                break
            idx = i if len(warehouse) % 2 == 0 else w - 1 - i  # 짝수층은 왼→오, 홀수층은 오→왼
            layer[idx] = box_num
            box_num += 1
        warehouse.append(layer)
    
    # 2. num이 어디에 있는지 찾기 (row, col)
    target_row, target_col = -1, -1
    for row in range(len(warehouse)):
        for col in range(w):
            if warehouse[row][col] == num:
                target_row, target_col = row, col
                break
        if target_row != -1:
            break

    # 3. 위에 있는 상자들 개수 + 자기 자신 = 정답
    count = 0
    for r in range(len(warehouse) - 1, -1, -1):  # 맨 위층부터 아래층까지
        if warehouse[r][target_col] != 0:
            count += 1
        if r == target_row:
            break

    return count
 
print(solution(22, 6, 8)) 