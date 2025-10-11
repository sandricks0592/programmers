def solution(hp):
    answer = 0
    general = 5
    soldier = 3
    worker = 1
    if hp % general >= 0:
        answer += hp // general
        if(hp % general) %soldier >= 0:
            answer += (hp % general) % soldier
            if((hp % general) % soldier) % worker >= 0:
                answer += ((hp % general) % soldier) % worker
    return answer
hp = 23
print(solution(hp))