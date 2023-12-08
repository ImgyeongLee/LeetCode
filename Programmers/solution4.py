# 문자열 내 마음대로 정렬하기
def solution1(strings, n):
    return sorted(strings, key=lambda word:(word[n], word))