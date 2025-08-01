n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target: # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        return binary_search(array, target, start, mid-1) 
    else: # 오른쪽 확인
        return binary_search(array, target ,mid+1, end)

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

# 예시 Input
# 10 7
# 1 3 5 7 9 11 13 15 17 19

# 예시 Output
# 4