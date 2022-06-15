def solution(a, b):
    answer = ''
    day_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    answer = day_of_week[(sum(day_of_month[:a]) + b) % 7]
    return answer


print(solution(5, 24))
