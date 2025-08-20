str = input()
new_str = ""

for i in range(len(str)):
    if str[i].islower():      # 소문자면
        new_str += str[i].upper()
    elif str[i].isupper():    # 대문자면
        new_str += str[i].lower()
    else:                   # 알파벳이 아니면 그대로
        new_str += str[i]

print(new_str)

# .is함수() 기억하기