from sys import stdin


def binary_search(target, data):
    start = 0
    end = len(data)-1

    while start <= end:
        mid = (start+end)//2

        if data[mid] == target:
            return target
        elif data[mid] < target:
            start = mid+1
        else:
            end = mid-1


N = int(stdin.readline().rstrip())
orig_cards = list(map(int, stdin.readline().rstrip().split()))

M = int(stdin.readline().rstrip())
compare_cards = set(map(int, stdin.readline().rstrip().split()))

# for card in compare_cards:
#     print('1' if card in orig_cards else '0', end=" ")

orig_cards.sort()

for card in compare_cards:
    idx = binary_search(card, orig_cards)

    print(idx, end=",")
    print('1' if idx else '0')
