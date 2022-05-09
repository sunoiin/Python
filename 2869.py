# V: 나무막대 높이
# A: 낮에 올라가는 높이
# B: 밤에 미끄러지는 높이

a, b, v = map(int, input().split())

day = v//(a-b)
h = 0

while(True):
    h = a*day-b*(day-1)
    if h < v:
        break
    day -= 1

print(day+1)


# a, b, v = map(int, input().split())
# print((v-b-1)//(a-b)+1)
