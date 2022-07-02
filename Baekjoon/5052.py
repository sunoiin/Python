T = int(input())

for _ in range(T):
    N = int(input())
    numbers = sorted([input() for _ in range(N)])

    answer = 'YES'
    for i in range(len(numbers)-1):
        if numbers[i+1].startswith(numbers[i]):
            answer = 'NO'

    print(answer)
