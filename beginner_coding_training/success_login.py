def solution(id_pw, db):
    answer = ''
    right_id = id_pw[0]
    right_pw = id_pw[1]
    for id, pw in db:
        if right_id == id and right_pw == pw:
            return "login"
        elif right_id == id and right_pw != pw:
            return "wrong pw"
    
    return "fail"

# 정의하는거 헷갈리지말기, 딕셔너리는 필요할때 사용하기, return을 내부에 사용하면 조건성공시 즉시 종료 가능