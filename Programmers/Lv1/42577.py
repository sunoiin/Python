# def solution(phone_book):
#     # 어떤 번호가 다른 번호의 접두어인 경우가 있으면 False
#     # 없으면 True

#     # 어떤 번호가 다른 번호의 접두어이기 위해서는, 글자수가 같거나 작아야 한다.
#     phone_book = sorted(phone_book, key=lambda x: len(x))

#     for num in range(len(phone_book)):
#         # 같은 전화번호는 중복되지 않는다. -> 만약 현재 번호와 전화번호부의 마지막 번호 글자수가 같으면, 접두어인 경우가 없다. (시간 줄일 수 있었음)
#         if len(phone_book[num]) == len(phone_book[-1]):
#             return True

#         for other_num in range(num + 1, len(phone_book)):
#             if phone_book[num] in phone_book[other_num]:
#                 if phone_book[num] == phone_book[other_num][:len(phone_book[num])]:
#                     # print(phone_book[num], phone_book[other_num])
#                     return False
#     # print(phone_book)
#     return True

### 대표답안 ###
def solution(phone_book):
    # 어떤 번호가 다른 번호의 접두어인 경우가 있으면 False / 없으면 True

    phone_book.sort()
    # 문자열의 같은 자리에서 아스키코드 순으로 정렬된다.
    # ['119', '97674223', '1195524421'] -> ['119', '1195524421', '97674223']

    for i, j in zip(phone_book, phone_book[1:]):
        # 뒤의 번호가 앞 번호로 시작하면, 접두어가 존재한다.
        if j.startswith(i):
            return False

    return True


print(solution(["119", "97674223", "1195524421"]))  # False
print(solution(["123", "456", "789"]))  # True
print(solution(["12", "123", "1235", "567", "88"]))  # False
