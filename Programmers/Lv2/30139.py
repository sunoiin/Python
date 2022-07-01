from collections import deque


def solution(maps):
    answer = 0

    h, w = len(maps), len(maps[0])

    visited = [[0]*w for _ in range(h)]
    visited[0][0] = 1

    queue = deque()
    queue.append([0, 0])

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        y, x = queue.popleft()  # 아직 방문하지 않은 곳 순서대로 방문

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:  # 새로운 좌표가 map을 벗어나지 않을 경우
                if visited[ny][nx] == 0 and maps[ny][nx] == 1:  # 좌표를 방문하지 않았고, 벽이 아닐 경우
                    visited[ny][nx] = visited[y][x] + 1  # 거리는 그 전 좌표까지의 거리 + 1
                    queue.append((ny, nx))  # 새로운 좌표를 queue에 추가

    if visited[h-1][w-1] == 0:  # (h, w)까지 방문하지 못한 경우
        answer = -1
    else:
        answer = visited[h-1][w-1]

    return answer


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
