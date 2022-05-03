c = int(input())

for i in range(c):
    data = list(map(int, input().split()))
    # data[0]은 학생 수니까, data[1:]를 socres라는 list로 따로 만들어주는 방법도 있음.
    # scores = list(map(int, data[1:]))
    # 대신에 나는 data[0]를 n_std라는 변수로 따로 할당했음.
    n_std = data[0]
    average = (sum(data)-n_std)/n_std
    count = 0
    for j in range(1, n_std+1):
        if data[j] > average:
            count += 1
    print(f"{count/n_std*100:.3f}%")
    # print(format(count/n_std*100, ".3f"), "%", sep="")
