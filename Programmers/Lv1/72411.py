from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:
        menu_dict = dict()
        # print(f"{c}개")
        for order in orders:
            # i보다 적게 주문하면 패스
            if len(order) < c:
                continue
            # i개 조합 만들기 dict로
            menu_comb = list(combinations(order, c))
            for i in menu_comb:
                comb = "".join(sorted(i))
                if comb in menu_dict:
                    menu_dict[comb] += 1
                else:
                    menu_dict[comb] = 1

        # print(menu_dict)

        max_value = 0
        for key, value in menu_dict.items():
            if int(value) > max_value:
                max_value = int(value)

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
