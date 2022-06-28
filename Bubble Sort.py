numbers = [6, 3, 8, 5, 2, 7, 4, 1]


cnt = 0
while(cnt < len(numbers)):
    cnt += 1
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            continue
    print(numbers)
