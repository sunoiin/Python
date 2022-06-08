def solution(record):
    answer = []
    id_name = dict()

    for rec in record:
        command = rec.split()[0]

        if command == "Leave":
            continue

        id = rec.split()[1]
        name = rec.split()[2]

        if command in ["Enter", "Change"]:
            id_name[id] = name

    for rec in record:
        command = rec.split()[0]
        id = rec.split()[1]

        if command == "Enter":
            name = rec.split()[2]
            answer.append(f"{id_name[id]}님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(f"{id_name[id]}님이 나갔습니다.")

    return answer


# Dict 자료형 활용
# 1. record[i][0] 명령어별 행동
#    record[i][1] -> dict.key (id)
#    record[i][2] -> dict.value (name)
# 2. 명령어별 행동
# 1) Enter: (id)의 (name)을 변경
# 2) Leave:
# 3) Change: (id)의 (name)을 변경
# 3. 결과 출력 -> answer
# record[i][0]

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
      "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
