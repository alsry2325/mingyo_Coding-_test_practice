n  = int(input())
cnt = 0
for i in range(n):
    cnt += 1
    print(cnt,end=" ")
    for j in range(i):
        cnt += 1
        print(cnt,end=" ")
    print()
    