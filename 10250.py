t = int(input())
# h: 호텔의 층  수
# w: 각 층의 방 수
# n: 몇 번째 손님인지

for _ in range(t):
    h, w, n = map(int, input().split())
    ww = (n-1)//h+1
    hh = (n-1) % h+1
    print(f"{hh}{str(ww).zfill(2)}")
