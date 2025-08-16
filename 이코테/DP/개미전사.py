# 구하는 것: 얻을 수 있는 식량의 최댓값
# 특정한 i번째 식량창고에 대해 약탈여부를 결정할 때, i-1번째 식량창고를 약탈한다면 -> i번째 식량창고 약탈 불가 / i-2번째 식량창고를 약탈한다면 -> i번째 식량창고 약탈 가능


n = int(input())
array = list(map(int, input().split()))

d = [0]*100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i  in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])

# 예시 Input
# 4
# 1 3 1 5

# 예시 Output
# 8