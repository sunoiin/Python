# 퇴사

n = int(input())
time_pay = []

for _ in range(n):
    time_pay.append(list(map(int, input().split())))
print(time_pay)

pay = 0
date = 0
while(True):
    date += time_pay[date][0]
    if date > n-1:
        break
    pay += time_pay[date][1]
print(pay)
