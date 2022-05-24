from sys import stdin

test_case = int(stdin.readline())

for _ in range(test_case):
    # n: 문서의 개수
    # m: 몇 번째로 인쇄되었는지 궁금한 문서
    # importance: 각 문서의 중요도
    n, m = map(int, stdin.readline().split())
    importance = list(map(int, stdin.readline().split()))
    order = 1
    for i in importance:
        if i > importance[m]:
            order += 1
    print(order)
