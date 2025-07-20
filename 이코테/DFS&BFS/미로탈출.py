from collections import deque

n, m = map(int, input().split())

# 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 방향을 튜플 리스트로 정의
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue: # 큐가 빌 때까지
        x, y = queue.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            # 종료: 범위 벗어남
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 종료: 벽인 경우
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))