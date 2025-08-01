input_data = input().split()
n = int(input_data[0])
target = input_data[1]

array = input().split()

def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 변환(인덱스는 0부터 시작하므로 1 더해줌)

print(sequential_search(n, target, array))

# 예시 Input
# 5 Dongbin
# Hanul Jonggu Dongbin Taeil Sangwook 

# 예시 Output
# 3