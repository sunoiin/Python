# 퇴사
# Dynamic Programming

# [1] 입력을 받습니다. 입력받은 n으로 t와 p라는 배열을 선언하고 들어오는 입력에 배열을 넣습니다.
n = int(input())
t, p = [0]*n, [0]*n

for i in range(n):
    t[i], p[i] = map(int, input().split())
print(t, p)

# [2] dynamic programming 방식으로 진행합니다. dp라는 배열을 생성하고 이 배열의 원소들은 해당 날에 받을 수 있는 최대의 보상을 저장하게 됩니다. 
# [3] dp는 현재 받게 될 보상과 내일 받게 될 보상을 비교합니다. 최대 수익을 구하기 때문에, 현재 받게 될 금액이 훨씬 더 클 경우 다음날 번 돈은 현재 금액으로 저장합니다.
# [4] 현재 기준으로 T일 이후에 받게 될 보상이 상담을 수행해서 받게 될 금액(P)보다 적다면 현재 금액(dp) + 상담 금액(P)로 저장합니다.

dp = [0]*25

for i in range(n):
    if dp[i] > dp[i+1]:  # 현재가 다음날보다 보상이 높다면
        dp[i+1] = dp[i]  # 다음날 보상은 현재로 (왜?)
    if dp[i+t[i]] < dp[i]+p[i]:  # T일 후에 받을 금액이 현재 보상보다 높다면
        dp[i+t[i]] = dp[i]+p[i]  # T일 후에 보상을 넣는다.

print(dp)
print(dp[n])
