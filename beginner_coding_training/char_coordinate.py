# def solution(keyinput, board):
#     answer = [0,0]
#     for i in keyinput:
#         if i == 'up':
#             answer = [answer[0],answer[1]+1]
#         elif i == 'down':
#             answer = [answer[0],answer[1]-1]
#         elif i == 'left':
#             answer = [answer[0]-1,answer[1]]
#         elif i == 'right':
#             answer = [answer[0]+1,answer[1]]
#     if answer[0]<board[0]//2 or board[0]//2<answer[0]:
#         answer = [board[0]//2,answer[1]]
#     elif answer[1]<board[1]//2 or board[1]//2<answer[1]:
#         answer = [answer[0],board[1]//2]
#     return answer

def solution(keyinput, board):
    answer = [0, 0]  # 캐릭터 시작 위치
    x_limit = board[0] // 2
    y_limit = board[1] // 2

    for key in keyinput:
        if key == 'up':
            answer[1] += 1
        elif key == 'down':
            answer[1] -= 1
        elif key == 'left':
            answer[0] -= 1
        elif key == 'right':
            answer[0] += 1

        # ✅ 이동 후 limit 초과 시 조정
        if answer[0] > x_limit:
            answer[0] = x_limit
        elif answer[0] < -x_limit:
            answer[0] = -x_limit

        if answer[1] > y_limit:
            answer[1] = y_limit
        elif answer[1] < -y_limit:
            answer[1] = -y_limit

    return answer

def solution2(keyinput, board):
    x_lim,y_lim = board[0]//2,board[1]//2
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            x,y = x+dx,y+dy

    return [x,y]

keyinput = ["left", "right", "up", "right", "right"]
board = [11,11]
print(solution(keyinput, board))

#  limit을 넘길때 조건을 따로 분리해주기, dic를 사용 할 수도 있다.