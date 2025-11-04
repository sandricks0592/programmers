def solution(bin1, bin2):
    answer = ''
    answer = int(bin1,2) + int(bin2,2)
    return bin(answer)[2:]
bin1 = '10'
bin2 = '11'
print(solution(bin1, bin2))

# 2진수로 이뤄진 문자열을 이진수로 인식시키는건 int('문자열",2)이고 십진수를 이진수로 바꾸려면 bin(정수)[2:]() '앞에 0b 제거'를 사용하면 된다.


