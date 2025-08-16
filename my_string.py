# 매개변수 string : my_string

my_string = input()
answer = []
def string_ascending ():
    answer = sorted([chr for chr in my_string if chr.isdigit()])
    return answer
    

print(answer)