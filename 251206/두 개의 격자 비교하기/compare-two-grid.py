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
    row = []
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            row.append(0)
        else:
            row.append(1)
    arr3.append(row)
for i in range(n):
    for j in range(m):
        print(arr3[i][j],end=" ")
    print()