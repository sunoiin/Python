N = int(input())
words = []
for i in range(N):
    word = input()
    if word not in words:
        words.append(word)
words = sorted(words, key=lambda x: (len(x), x))
print(*words, sep='\n')
