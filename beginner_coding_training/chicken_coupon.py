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

# 