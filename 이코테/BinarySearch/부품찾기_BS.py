n = int(input())
array = list(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

array.sort() # 이진탐색하기위한 정렬

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
    
for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

# 예시 Input
# 5
# 8 3 7 9 2
# 3
# 5 7 9

# 예시 Output
# no yes yes 