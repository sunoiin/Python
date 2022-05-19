n = int(input())
numbers = list()
sorted_numbers = list()

for _ in range(n):
    numbers.append(int(input()))


for i in range(n):
    for j in range(n):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

for i in numbers:
    print(i)
