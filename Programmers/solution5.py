# 최댓값과 최솟값
def solution1(s):
    numbers = list(map(int, s.split(" ")))
    return f"{min(numbers)} {max(numbers)}"

# JadenCase 문자열 만들기
def solution2(s):
    strings = s.split(" ")
    answer = []
    for string in strings:
        answer.append(string.capitalize())

    return " ".join(answer)

if __name__ == "__main__":
    print(solution2("3people unFollowed me"))