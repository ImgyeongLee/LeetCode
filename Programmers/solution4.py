import random
# 문자열 내 마음대로 정렬하기
def solution1(strings, n):
    return sorted(strings, key=lambda word: (word[n], word))


# 2016년
def solution2(a, b):
    days = ["FRI", "FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month_data = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Jan 1st is Friday

    current_month = 1
    current_date = 1

    while current_month < a:
        current_date += 7

        if current_date > month_data[current_month]:
            current_date -= month_data[current_month]
            current_month += 1

    while current_date < b:
        diff = abs(current_date - b)
        if diff > 7:
            current_date += 7
        elif diff == 7:
            return days[1]
        else:
            return days[diff + 1]

    return days[b - current_date]


# 모의고사
def solution3(answers):
    record = {"1": 0, "2": 0, "3": 0}
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    first_idx = 0
    second_idx = 0
    third_idx = 0

    first_max = len(first)
    second_max = len(second)
    third_max = len(third)

    for i in range(0, len(answers)):
        if answers[i] == first[first_idx]:
            record["1"] += 1
        if answers[i] == second[second_idx]:
            record["2"] += 1
        if answers[i] == third[third_idx]:
            record["3"] += 1

        first_idx += 1
        second_idx += 1
        third_idx += 1

        if first_idx >= first_max:
            first_idx = 0
        if second_idx >= second_max:
            second_idx = 0
        if third_idx >= third_max:
            third_idx = 0

    sorted_record = dict(sorted(record.items(), key=lambda x: x[1], reverse=True))
    result = []
    maxVal = 0
    for key in sorted_record:
        if len(result) == 0:
            result.append(int(key))
            maxVal += int(sorted_record[key])
        elif maxVal != sorted_record[key]:
            return result
        else:
            result.append(int(key))

    return result


# 실패율
def solution4(N, stages):
    sorted_stages = sorted(stages)
    total = len(stages)
    count = 0
    stage = 1
    idx = 0

    data = {}

    while stage <= N:
        if total <= 0:
            data[stage] = 0
            stage += 1
        elif idx >= len(sorted_stages) or stage != sorted_stages[idx]:
            data[stage] = count / total
            total -= count
            count = 0
            stage += 1
        else:
            count += 1
            idx += 1

    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    result = []

    for data in sorted_data:
        result.append(data[0])

    return result


# 체육복
def solution5(n, lost, reserve):
    filtered_lost = list(set(lost) - set(reserve))
    filtered_reserve = list(set(reserve) - set(lost))

    for student in filtered_lost:
        if student - 1 in filtered_reserve:
            filtered_reserve.remove(student - 1)
        elif student + 1 in filtered_reserve:
            filtered_reserve.remove(student + 1)
        else:
            n -= 1

    return n


# 크레인 인형 뽑기
def solution6(board, moves):
    inventory = []
    count = 0
    for move in moves:
        selected_col = list(zip(*board))[move - 1]
        col_len = len(selected_col)
        for i in range(0, col_len):
            if selected_col[i] != 0:
                inventory.append(selected_col[i])
                board[i][move - 1] = 0
                break

    cur = 0
    # organize the array
    while True:
        if cur + 1 < len(inventory):
            if inventory[cur] == inventory[cur + 1]:
                count += 2
                inventory = inventory[0:cur] + inventory[cur + 2:]
                cur = 0
            else:
                cur += 1
        else:
            break

    return count


# 키패드 누르기
def solution7(numbers, hand):
    isLeft = False
    if hand == "left":
        isLeft = True

    position = {"1": (0, 0), "2": (0, 1), "3": (0, 2),
                "4": (1, 0), "5": (1, 1), "6": (1, 2),
                "7": (2, 0), "8": (2, 1), "9": (2, 2),
                "*": (3, 0), "0": (3, 1), "#": (3, 2)}

    left_digit = [1, 4, 7]
    right_digit = [3, 6, 9]

    right_cur_pos = position["*"]
    left_cur_pos = position["#"]

    answer = []

    for number in numbers:
        if number in left_digit:
            answer.append("L")
            left_cur_pos = position[str(number)]
        elif number in right_digit:
            answer.append("R")
            right_cur_pos = position[str(number)]
        else:
            num_pos = position[str(number)]
            left_dist = abs(num_pos[0] - left_cur_pos[0]) + abs(num_pos[1] - left_cur_pos[1])
            right_dist = abs(num_pos[0] - right_cur_pos[0]) + abs(num_pos[1] - right_cur_pos[1])

            if left_dist < right_dist:
                answer.append("L")
                left_cur_pos = position[str(number)]

            elif left_dist > right_dist:
                answer.append("R")
                right_cur_pos = position[str(number)]

            else:
                answer.append("L" if isLeft else "R")
                if isLeft:
                    left_cur_pos = position[str(number)]
                else:
                    right_cur_pos = position[str(number)]

    return "".join(answer)


# 신규 아이디 추천
def solution8(new_id):
    valid_character = ["-", "_", "."]
    temp = ""

    # phase 1 and phase 2
    for character in new_id:
        if character.isalpha():
            if ord(character) < 97:
                temp += chr(ord(character) + 32)
            else:
                temp += character

        if character.isdigit() or character in valid_character:
            temp += character

    # update new_id
    new_id = temp

    # phase 3
    temp = ""
    dot_concat_flag = False

    for character in new_id:
        if dot_concat_flag:
            if character != ".":
                dot_concat_flag = False
                temp += character
        else:
            if character == ".":
                dot_concat_flag = True
                temp += character
            else:
                temp += character

    new_id = temp

    # phase 4
    if len(new_id) > 0:
        if len(new_id) == 1:
            if new_id[0] == ".":
                new_id = ""
        else:
            if new_id[0] == ".":
                new_id = new_id[1:]
            if new_id[len(new_id) - 1] == ".":
                new_id = new_id[:(len(new_id) - 1)]

    # phase 5
    if len(new_id) == 0:
        new_id += "a"

    # phase 6
    if len(new_id) > 15:
        new_id = new_id[:15]

        if new_id[len(new_id) - 1] == ".":
            new_id = new_id[:(len(new_id) - 1)]

    # phase 7
    if len(new_id) < 3:
        last_character = new_id[len(new_id) - 1]
        while len(new_id) < 3:
            new_id += last_character

    return new_id


# 성격 유형 검사하기
def solution9(survey, choices):
    # 1번 지표
    # 라이언형(R), 튜브형(T)
    # 2번 지표
    # 콘형(C), 프로도형(F)
    # 3번 지표
    # 제이지형(J), 무지형(M)
    # 4번 지표
    # 어피치형(A), 네오형(N)

    personality_record = {"R": 0, "T": 0,
                          "C": 0, "F": 0,
                          "J": 0, "M": 0,
                          "A": 0, "N": 0}

    score_mid = 4
    choice_idx = 0

    for problem in survey:
        score = choices[choice_idx] - score_mid
        if score < 0:
            personality_record[problem[0]] += abs(score)
        elif score > 0:
            personality_record[problem[1]] += score
        choice_idx += 1

    result = ""

    if personality_record["R"] >= personality_record["T"]:
        result += "R"
    else:
        result += "T"

    if personality_record["C"] >= personality_record["F"]:
        result += "C"
    else:
        result += "F"

    if personality_record["J"] >= personality_record["M"]:
        result += "J"
    else:
        result += "M"

    if personality_record["A"] >= personality_record["N"]:
        result += "A"
    else:
        result += "N"

    print(personality_record)

    return result


# 개인정보 수집 기간
def solution10(today, terms, privacies):
    # 0: year 1: month 2: date
    today_list = today.split(".")
    today_date = int(today_list[0]) * 12 * 28 + int(today_list[1]) * 28 + int(today_list[2])

    term_data = {}
    privacy_list = []

    for term in terms:
        term_name = term.split(" ")[0]
        term_data[term_name] = int(term.split(" ")[1])

    for privacy in privacies:
        data = {}
        date_list = (privacy.split(" ")[0]).split(".")
        converted_date = int(date_list[0]) * 12 * 28 + int(date_list[1]) * 28 + int(date_list[2])
        data["term"] = privacy.split(" ")[1]
        data["date"] = converted_date
        privacy_list.append(data)

    idx = 1
    answer = []

    for data in privacy_list:
        valid_date = data["date"] + term_data[data["term"]] * 28
        if valid_date - 1 < today_date:
            answer.append(idx)

        idx += 1

    return answer


# 신고 결과 받기
def solution11(id_list, report, k):
    record = {}
    mailing = {}
    for id in id_list:
        record[id] = []
        mailing[id] = 0

    for rep in report:
        report_list = rep.split(" ")
        if not report_list[0] in record[report_list[1]]:
            record[report_list[1]].append(report_list[0])

    for id in id_list:
        if len(record[id]) >= k:
            for user in record[id]:
                mailing[user] += 1

    return list(mailing.values())
def betting(n):
    betting_arr = [3, 2, 2, 1, 1, 1, 0, 0, 0, "특별상품"]
    random_number = random.randint(0, 9)

    print(random_number)

    # 특별상품 당첨 시
    if random_number == 9:
        return betting_arr[random_number] + "에 당첨되셨습니다. 총괄계를 멘션해주세요!"
    # 그 이외
    else:
        result = betting_arr[random_number] * n
        return str(result) + "에클을 얻으셨습니다."

if __name__ == "__main__":
    print(betting(2))