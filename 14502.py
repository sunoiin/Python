# 벽 세우기 (반복문))
# 0. '0'인 지점에 차례대로 3개의 벽을 세운다.
# <DFS>
# 1. 바이러스 지점의 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다.
# 2. 방문한 지점에서 다시 상,하,좌,우를 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점을 방문 할 수 있다.
# 3. 모든 바이러즈 지점에 대해 1~2번의 과정을 반복하며, 안전 영역(0)의 최댓값을 구한다.

# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

def dfs(x, y):
  # 주어진 범위를 벗어나는 경우 즉시 종료
    # if x <= -1 or x >= N or y <= -1 or y >= M:
    #     return False

  # 현재 노드를 아직 방문하지 않았따면
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 2
            dfs(nx, ny)
            return True


N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

# 벽 3개 세우기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            graph[i][j] = 1

# 바이러스로 퍼지기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            dfs(i, j)

print(*graph, sep="\n")
