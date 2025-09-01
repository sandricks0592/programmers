a,b = map(int,input().split(" "))
def solution():
    answer = 0
    ab = str(a)+str(b)
    ba = str(b)+str(a)
    if int(ab >= ba):
        answer = ab
    else:
        answer = ba
    
    return int(answer)


print(solution())
