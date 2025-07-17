# 0인 값이 상하좌우로 연결되어있는 노드 묶음의 개수를 찾자!

# 특정한 지점의 주변 상하좌우를 살펴본 뒤에 주변 지점 중에서 값이 아직 0이면서 방문하지 않은 지점이 있다면 그 지점을 방문한다.
# 방문한 지점에서 다시 상하좌우를 살펴보며 방문을 진행
# 방문하지 않은 지점의 수를 센다

n, m = map(int, input().split())

# 맵 정보 입력받기
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    # 종료조건 1
    if x<0 or x>=n or y<0 or y>=m:
        return False  

    # 성공조건  
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x,y-1) # 좌
        dfs(x,y+1) # 우
        dfs(x-1,y) # 상
        dfs(x+1,y) # 하
        return True
      
    # 종료조건 2
    return False  

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)