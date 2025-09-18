def solution(names):
    answer = []
    for i in range(0,len(names),5):
        answer.append(names[i])
    return answer

names = ["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]
print(solution(names))