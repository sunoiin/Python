def solution(s):
    # 대소문자 구분이 없으므로 모두 소문자로 바꾼다.
    s = s.lower()

    # p, y 모두 하나도 없는 경우도 아래 조건에 포함된다. 따로 조건 작성할 필요 없음.
    if s.count('p') == s.count('y'):
        return True
    else:
        return False
