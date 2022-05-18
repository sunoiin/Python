n = int(input())

# i = 666  # 1
# cnt = 0

# while(True):
#     if i//10 == 666 or i//100 == 666 or i//1000 == 666 or i//10000 == 666 or i % 1000 == 666 or i//10 % 1000 == 666 or i//100 % 1000 == 666 or i//1000 % 1000 == 666:
#         cnt += 1  # 2
#     if cnt == n:
#         print(i)
#         break  # 3
#     i += 1

series_num = 666
cnt = 0

while True:
    if '666' in str(series_num):
        cnt += 1
    if cnt == n:
        print(series_num)
        break
    series_num += 1
