# 단어를 입력받고 대문자로 변환한다.
word = input()
word = word.upper()

# 각 alphabet의 아스키코드를 인덱스로 갖는 list를 생성한다.
alphabet = [0 for _ in range(91)]

# 문자열 i가 포함될 경우 요소를 1씩 더한다.
for i in word:
    alphabet[ord(i)] += 1

# 가장 많이 사용된 알파벳의 사용 횟수를 구한다.
max = max(alphabet)

# 최대값이 여러개일 경우 '?'를 출력한다.
if alphabet.count(max) > 1:
    print('?')
# 최대값이 1개일 경우 해당 값의 인덱스를 유니코드로 변환하여 출력한다.
else:
    tmp = max
    index = alphabet.index(tmp)
    print(chr(index))
