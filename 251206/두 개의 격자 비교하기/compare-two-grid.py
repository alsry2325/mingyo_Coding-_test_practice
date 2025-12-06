n,m = map(int,input().split())

arr1 = []
arr2 = []
arr3 = []
for _ in range(n):
    results = list(map(int,input().split()))
    arr1.append(results)

for _ in range(n):
    results = list(map(int,input().split()))
    arr2.append(results)

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            arr3.append(0)
        else:
            arr3.append(1)
print(*arr3[0:4])
print(*arr3[4:8])
print(*arr3[8:12])
print(*arr3[12:16])