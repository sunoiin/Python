from sys import stdin

test_case = int(stdin.readline())

for _ in range(test_case):
    # n: 문서의 개수
    # m: 몇 번째로 인쇄되었는지 궁금한 문서
    # imp: 각 문서의 중요도
    # idx: 인쇄 명령을 받은 순서
    n, m = map(int, stdin.readline().split())
    imp = list(map(int, stdin.readline().split()))
    idx = [i for i in range(n)]

    order = 0

    while(True):
        if imp[0] == max(imp):
            order += 1

            if idx[0] != m:
                del imp[0]
                del idx[0]
            else:
                print(order)
                break
        else:
            imp.append(imp[0])
            idx.append(idx[0])
            del imp[0]
            del idx[0]
