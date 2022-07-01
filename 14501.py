# 퇴사
# Dynamic Programming

n = int(input())
t, p = [0]*n, [0]*n

for i in range(n):
    t[i], p[i] = map(int, input().split())
print(t)
print(p)

# [2] dynamic programming.
# dp라는 배열을 생성하고 이 배열의 원소들은 해당 날에 받을 수 있는 최대의 보상을 저장한다.
dp = [0]*25

for i in range(n):
    # [3] T일 이후에 받게 될 보상이 상담을 수행해서 받게 될 금액(P)보다 적다면
    # 현재 금액(dp) + 상담 금액(P)로 저장한다.
    if dp[i+t[i]] < dp[i]+p[i]:  # T일 후에 받을 금액이 현재 보상보다 높다면
        dp[i+t[i]] = dp[i]+p[i]  # T일 후에 보상을 넣는다.

    # [4] 현재 받게 될 보상과 내일 받게 될 보상을 비교.
    # if dp[i] > dp[i+1]:  # 현재가 다음날보다 보상이 높다면
    #     dp[i+1] = dp[i]  # 다음날 보상은 현재로
    print(dp)


# print(dp)
print(dp[n])
