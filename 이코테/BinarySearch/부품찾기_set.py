n = int(input())
array = set(map(int, input().split())) # set은 해시 테이블 기반이라 탐색이 빠름
m = int(input())
x = list(map(int, input().split()))

for i in x: 
    if i in array:
        print('yes', end = ' ')
    else: 
        print('no', end = ' ')