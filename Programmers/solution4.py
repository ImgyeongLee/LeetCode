# 문자열 내 마음대로 정렬하기
def solution1(strings, n):
    return sorted(strings, key=lambda word:(word[n], word))


def solution3(N, stages):
    player_num = len(stages)
    data_set = {}
    for stage in stages:
        if N < stage:
            continue
        if stage in data_set:
            data_set[stage] += 1
        else:
            data_set[stage] = 1


    return data_set


if __name__ == "__main__":
    print(solution3(2, [2, 1, 2, 6, 2, 4, 3, 3]))