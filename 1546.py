import sys


n = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
m = max(scores)

new_scores = [score/m*100 for score in scores]

print(sum(new_scores)/len(new_scores))
