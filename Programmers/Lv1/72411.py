from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:
        menu_dict = dict()
        # print(f"{c}개")
        for order in orders:
            # 만약 주문한 메뉴 수가 코스 메뉴 수보다 적을 경우 패스
            if len(order) < c:
                continue
            # 단품 c개로 구성된 코스요리의 조합 구하기
            menu_comb = list(combinations(order, c))

            for i in menu_comb:
                comb = "".join(sorted(i))
                # 각 사람이 주문한 코스요리 조합 더하기
                if comb in menu_dict:
                    menu_dict[comb] += 1
                else:
                    menu_dict[comb] = 1

        # print(menu_dict)

        max_value = 0
        # 단품 c개로 구성된 코스요리 중 최다 주문 조합 구하기
        for key, value in menu_dict.items():
            if int(value) > max_value:
                max_value = int(value)

        # 만약 최다 주문이 2보다 작을 경우 무시
        # 최다 주문 조합을 코스요리로 구성한다.
        for key, value in menu_dict.items():
            if value < 2:
                continue
            elif value == max_value:
                answer.append(key)

        answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
