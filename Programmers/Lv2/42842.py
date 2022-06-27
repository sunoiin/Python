# 카펫의 테두리는 갈색으로 칠해져 있고, 안쪽은 노란색으로 칠해져 있다.
# 갈색, 노란색으로 색칠된 격자의 개수가 주어질 때 카펫의 가로, 세로 크기를 구하여라.
# 가로 >= 세로

def solution(brown, yellow):
    answer = []

    total = brown + yellow

    # 가로는 3 이상, total//3 이하이다.
    for w in range(3, total//3 + 1):
        # 전체 넓이가 가로 길이로 나누어 떨어지지 않으면 continue
        if total % w != 0:
            continue

        h = total // w

        # 안쪽에 칠해진 노란색 격자 개수가 동일하면, 가로 세로 리턴
        if ((w-2) * (h-2)) == yellow:
            answer = [max(w, h), min(w, h)]
            break

    return answer
