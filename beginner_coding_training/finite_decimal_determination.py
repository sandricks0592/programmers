def solution(a, b):
    # 1. 최대공약수 구하기 (유클리드 호제법)
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    g = gcd(a, b)
    b //= g  # 기약분수로 만들기 위해 분모 축소

    # 2. 2와 5로 나누기
    for p in [2, 5]:
        while b % p == 0:
            b //= p

    # 3. 남은 수 확인
    if b == 1:
        return 1  # 유한소수
    else:
        return 2  # 무한소수


a = 12
b = 21

print(solution(a, b))

# 유클리드 호제법을 생각하기, 나머지 값 활용하는 것 생각하기, import를 못 할 경우 함수를 하나 만들기.