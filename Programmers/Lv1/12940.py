def solution(n, m):
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            gcd = i
            break
    for i in range(max(n, m), n*m+1):
        if i % n == 0 and i % m == 0:
            lcm = i
            break
    return [gcd, lcm]


print(solution(3, 12))
print(solution(2, 5))
print(solution(4, 12))
print(solution(6, 7))
