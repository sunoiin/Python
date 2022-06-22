def solution(strings, n):
    print(strings, end=" -> ")
    strings = sorted(strings)
    answer = sorted(strings, key=lambda a: a[n])

    return answer


print(solution(["sun", "bed", "car"], 1))  # ['car', 'bed', 'sun']
print(solution(["abce", "abcd", "cdx"], 2))  # ['abcd', 'abce', 'cdx']
