def solution(sizes):
    # answer = max((max(size) for size in sizes) * (min(size) for size in sizes))
    max_w, max_h = 0, 0
    for size in sizes:
        size.sort(reverse=True)
        max_w = max(size[0], max_w)
        max_h = max(size[1], max_h)
    answer = max_w * max_h
    return answer


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))  # 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))  # 120
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))  # 133
