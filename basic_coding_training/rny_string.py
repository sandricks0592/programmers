def solution(rny_string):
    answer = ''
    rny_string = list(rny_string)
    for i in range(len(rny_string)):
        if rny_string[i] == 'm':
            answer += 'rn'
        else:
            answer += rny_string[i]
    return "".join(answer)

rny_string = "masterpiece"
print(solution(rny_string))