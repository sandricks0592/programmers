def solution (chicken):
    service = 0
    remain = 0
    while chicken >= 10:
        new = chicken // 10
        service += new
        chicken = new + (chicken % 10)
    return service

chicken = 100
print(solution (chicken))

# 치킨 양과 서비스 횟수를 따로 생각하기