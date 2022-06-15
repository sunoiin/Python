def solution(price, money, count):
    # answer = -1
    # new_price = price
    # for i in range(1, count+1):
    #     money -= new_price
    #     new_price += price
    # answer = (-money)
    # if answer < 0:
    #     return 0
    # else:
    #     return answer

    pay = 0
    for i in range(1, count+1):
        pay += (price * i)
    if money < pay:
        return pay - money
    else:
        return 0
