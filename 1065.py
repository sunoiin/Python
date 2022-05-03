n = 110

for i in range(100, n+1):
    if i < 100:
        print(i)
    else:
        print(i)
        while i >= 10:
            n = i % 10
            i = i//10
            diff = i % 10-n
            print(diff)

            # diff += i
            # print(diff)

# 101 102 103 104 105 106 107 108 109
