N = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(N)
]


for a,b in arr:
    total = 0
    for i in range(a,b+1):
        if i % 2 == 0:
            total+=i
    print(total)
