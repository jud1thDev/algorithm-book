n, m, k = map(int, input().strip().split())
numlist = list(map(int, input().strip().split()))

numlist.sort()
first = numlist[n-1]
second = numlist[n-2]
result = 0
tmpk = 0

for i in range(m):
    if tmpk == 0: 
        result += second
        tmpk = k
    else: 
        result += first
        tmpk -= 1
    print(result, tmpk) #테스트용

print(result)
