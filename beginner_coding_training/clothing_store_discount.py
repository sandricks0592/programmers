def solution(price):
    if price >= 500000:
        answer = price * 0.8     # 20% 할인
    elif price >= 300000:
        answer = price * 0.9     # 10% 할인
    elif price >= 100000:
        answer = price * 0.95    # 5% 할인
    else:
        answer = price
    return int(answer)  # 정수로 반환

# 나누기를 사용하는것보다 소수점을 이용하자. 그리고 마무리는 int를 사용하자.