arr = [
    list(map(int,input().split()))
    for _ in range(4)
]

total = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if j <= i:  #j가 0부터 i까지
            total+=arr[i][j]
print(total)
            
    
        