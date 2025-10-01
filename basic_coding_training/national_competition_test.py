def solution(rank, attendance):
    answer = 0
    num = []
    competition = []
    for i in range(len(rank)):
        num.append(i)
    for k,v,n in zip(rank,attendance,num):
        if v :
            competition.append((k,n))
    competition.sort(key=lambda x: x[0])
    first, second, third = competition[0][1], competition[1][1], competition[2][1]
    answer = 10000 * first + 100 * second + third
    return answer

rank = [3, 7, 2, 5, 4, 6, 1]
attendance = [False, True, True, True, True, False, False]
print(solution(rank, attendance))

#  다차원 배열에서  k,v,i,값을 사용하는 방법 익숙해지기