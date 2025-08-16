# korean : now_year - year + 1
# year_age : now_year - year
# 출생 연도 year
# 구하려는 나이의 종류를 나타내느 문자열 age_type
# korea or year

year = int(input())
age_type = input()

def your_age(year,age_type):
    if age_type == 'Korea' or 'korea':
        answer = 2030 - year + 1
        return(answer)
    elif age_type == 'Year' or 'year':
        answer = 2030 - year
        return(answer)
    else :
        return 0

print(your_age(year,age_type))

