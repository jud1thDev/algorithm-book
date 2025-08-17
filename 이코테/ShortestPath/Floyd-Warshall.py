# 다익스트라는 '한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우', 그리디
# 플로이드워셜은 '모든 지점에서 다른 모든 지점까지의 최단 경로', DP 

INF= int(1e9)


n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드워셜
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINETY")
        else: 
            print(graph[a][b], end = " ")
    print() # 줄바꿈

# 예시 Input
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4 
# 4 3 2

# 예시 Output
# 0 4 8 6 
# 3 0 7 9
# 5 9 0 4
# 7 11 2 0