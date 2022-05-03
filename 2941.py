word = input()

c = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
c2 = 'dz='

num = len(word)
count = 0
for i in range(len(word)-1):
    new_word = word[i]+word[i+1]
    # 단어를 두글자씩 조합했을 때, 크로아티아 알파벳이면 전체 알파벳 수를 -1씩 감소
    if new_word in c:
        num -= 1
        # 'z='가 포함될 경우, 'dz='가 만들어지는지 확인 후 -1 감소
        if i > 0 and word[i-1]+new_word == c2:
            num -= 1

print(num)
