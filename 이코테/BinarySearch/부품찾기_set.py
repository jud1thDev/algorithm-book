n = int(input())
array = set(map(int, input().split())) # set 집합은 중복 허용하지 않으므로, 트겆ㅇ 데이터가 존재하는지 검사할 때 효과적
m = int(input())
x = list(map(int, input().split()))

for i in x: 
    if i in array:
        print('yes', end = ' ')
    else: 
        print('no', end = ' ')