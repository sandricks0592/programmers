# 저수지에 저장된 물의 양 : int storage
# 지난 달 물 사용량을 나타내는 정수 : int usage
# 월별 물 사용량이 전 달 대비 어떻게 변하는지 : int list change

def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage = total_usage * change[i]/100
        total_usage += usage
        if total_usage  storage:
            return i
    
    return -1
