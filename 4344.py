c = int(input())

for i in range(c):
    scores = list(map(int, input().split()))
    n_std = scores[0]
    avg = (sum(scores)-n_std)/n_std
    count = 0
    for j in range(1, n_std):
        if scores[j] >= avg:
            count += 1
    print(format(count/n_std*100, ".3f"), "%", sep="")
