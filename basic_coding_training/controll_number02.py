def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        diff = numLog[i+1] - numLog[i]
        if diff == 1:
            answer += 'w'
        elif diff == -1:
            answer += 's'
        elif diff == 10:
            answer += 'd'
        elif diff == -10:
            answer += 'a'
    return answer

numLog = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]

print(solution(numLog))