# 집합 자료형 set() 사용
d_n = set([])

# 1부터 10000까지의 생성자로 만들 수 있는 d(n) 집합을 생성한다.
# 아래 반복문은 일의자리부터 천의자리 숫자까지 더한다.
for n in range(1, 10000):
    answer = n
    while n >= 10:
        answer += n % 10
        n = n // 10
    answer += n
    d_n.add(answer)

# 1부터 10000까지 전체 숫자로 이루어진 집합을 생성한다.
all_number = set(i for i in range(1, 10000))

# 차집합을 이용해 self number 집합을 구하고, 오름차순 정렬 후 출력한다.
self_number = all_number-d_n
self_number = sorted(self_number)

for i in self_number:
    print(i)
