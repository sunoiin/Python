# n = int(input())
# group_word = n

# for _ in range(n):
#     word = input()

#     if len(word) <= 2:
#         continue

#     count = list(0 for i in range(123))

#     c = word[0]
#     count[ord(c)] += 1
#     i = 0
#     while(True):
#         if word[i+1] == c:
#             i += 1
#             continue
#         else:
#             c = word[i+1]
#             if count[ord(c)] != 0:
#                 group_word -= 1
#                 break
#             count[ord(c)] += 1
#             i += 1
#         if i == len(word)-1:
#             break

# print(group_word)

n = int(input())
cnt = 0

for i in range(n):
    alphabet = [0 for _ in range(123)]
    word = input()
    for a in range(len(word)):
        if alphabet[ord(word[a])] != 0:
            if word[a] != word[a-1]:
                cnt += 1
                break
            else:
                continue
        alphabet[ord(word[a])] += 1

print(n-cnt)
