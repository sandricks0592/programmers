def solution(spell, dic):
    spell_sorted = ''.join(sorted(spell))  # spell 정렬 후 문자열로 변환

    for word in dic:
        if ''.join(sorted(word)) == spell_sorted:
            return 1
    return 2

spell = ["p", "o", "s"]
dic = ["sod", "eocd", "qixm", "adio", "soo"]
print(solution(spell, dic))