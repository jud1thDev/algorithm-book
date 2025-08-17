# 우선순위 큐 -> PriorityQue 또는 heapq 라이브러리에서 지원하는데, 일반적으로 heapq가 더 빠르므로 코테에서 권장
# 최소 힙을 최대 힙처럼 사용하려면 우선순위에 해당하는 값에 - 를 붙인다

import heapq
import sys
input = sys.stdin.readline
INF= int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a번 노드에서 b번 노드로 가는 비용이 c

distance = [INF]*(n+1) # 최단거리 테이블 초기값

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now] < dist: # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINETY")
    else: 
        print(distance[i])

# 예시 Input
# 6 11
# 1
# 1 2 2 
# 1 3 5
# 1 4 1
# 2 3 3 
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2

# 예시 Output
# 0
# 2
# 3
# 1
# 2
# 4

