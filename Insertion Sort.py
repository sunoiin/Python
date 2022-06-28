numbers = [6, 3, 8, 5, 2, 7, 4, 1]

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[j] == min(numbers[i:]):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            continue
    print(numbers)
