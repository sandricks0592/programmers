# 산책 루트가 담긴 문자열 route
# route는 "N", "S", "E", "W"로 이루어져 있습니다.
# "N"은 북쪽으로 1만큼 움직입니다.
# "S"는 남쪽으로 1만큼 움직입니다.
# 북쪽으로 -1만큼 움직인 것과 같습니다.
# "E"는 동쪽으로 1만큼 움직입니다.
# "W"는 서쪽으로 1만큼 움직입니다.
# 동쪽으로 -1만큼 움직인 것과 같습니다.

def solution(route):
    east = 0
    north = 0
    for i in route:
        if i == "N":
            north += 1
        elif i == "S" :
            north -= 1
        elif i == "E" :
            east += 1
        elif i == "W" :
            east -= 1

    return [east, north]